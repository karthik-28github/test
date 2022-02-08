
@router.post("/export-csv-campaign-history/")
def export_csv_campaign_history(data: Dict, ids: Tuple = Depends(get_current_user), db: Session = Depends(get_db)):
    response = {}
    response['status'] = 500
    filter_type = data.get('filter_type', None)
    campaign_id = data.get('campaign_id', '')
    start_date = data.get('start_date', None)
    end_date = data.get('end_date', None)
    campaign_type = data.get('campaignType', '')
    campaign_name=data.get("campaignName","")
    status = data.get("campaignStatus","")

    try:
        logger.info("export_csv_campaign_history %s",str(data))

        user_id = ids[0]
        tenant_id = ids[1]
        sub_domain = ids[3]

        history_objs = db.query(CampaignTransaction, Campaign).options(
						joinedload(CampaignTransaction.unit_campaign_transaction)).options(
						joinedload(CampaignTransaction.campaign)).options(
						joinedload(CampaignTransaction.approver1)).options(
						joinedload(CampaignTransaction.approver2)).options(
						joinedload(CampaignTransaction.campaign_value).joinedload(CampaignValue.value)).options(
						joinedload(CampaignTransaction.ecard)).join(
                        Campaign, Campaign.id == CampaignTransaction.campaign_id).join(
                        Tenant, Tenant.id == Campaign.tenant_id).filter(
                        Tenant.id == tenant_id).order_by(desc(CampaignTransaction.date_created))

        logger.error('.......................',history_objs.count())
        if start_date and end_date:
            start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y").strftime("%Y-%m-%d")

        if filter_type:
            interval = filter_type
            if interval != Interval.CUSTOM:
                start_date, end_date = get_from_to_dates_from_interval(interval)

        if campaign_type!="":
            history_objs = history_objs.filter(Campaign.campaign_type == campaign_type)

        if campaign_id!="":
            history_objs = history_objs.filter(Campaign.id == campaign_id)

        if campaign_name!="":
            history_objs = history_objs.filter(Campaign.name.like('%' + campaign_name + '%'))

        if status!="":
            history_objs = history_objs.filter(CampaignTransaction.approver_status == status)

        if start_date:
            history_objs = history_objs.filter(CampaignTransaction.date_created >= start_date)

        if end_date:
            history_objs = history_objs.filter(CampaignTransaction.date_created <= end_date)



        fieldnames= [
                        'tenantName','campaignName','camaignID','description','status','campaignType','sendingDate','documentUrl','sender',
                        'senderEmail','senderComment','approver1','approver1Email','approval_1date','approver2','approver2Email','approval_2date','approver1Comment','approver2Comment',
                        'receiever','receiverEmail','points_awarded','remainingBudget','valueName','ecardTemplateName','ecardUrl'
                    ]
        

        tenant_name = sub_domain.split('.')[0].title()
        history_csv = []
        user_id_list = []

        for history_obj, campaign_obj in history_objs:
            Campaign_approver_obj = db.query(CampaignApprover).filter(and_(
                CampaignApprover.campaign_id == campaign_obj.id, CampaignApprover.user_id == user_id)).first()

            temp_dict={}
            temp_dict['tenantName'] = tenant_name
            temp_dict['remainingBudget'] = ''
            temp_dict['approval_1date'] = ''
            temp_dict['approval_2date'] = ''
            temp_dict['camaignID'] = campaign_obj.id
            temp_dict['campaignName'] = campaign_obj.name
            temp_dict['description'] = campaign_obj.description
            temp_dict['status'] = history_obj.approver_status
            temp_dict['campaignType'] = campaign_obj.campaign_type
            temp_dict['sendingDate'] = datetime.datetime.strftime(history_obj.date_created, "%d-%m-%Y")
            temp_dict['documentUrl'] = history_obj.document_url
            temp_dict['sender'] = str(history_obj.sender_id)
            temp_dict['senderEmail'] = ''
            if history_obj.sender_id != "":
                user_id_list.append(str(history_obj.sender_id))

            temp_dict['senderComment'] = history_obj.description
            temp_dict['approver1']=str(history_obj.approver1.user_id) if history_obj.approver1_id!=None else ""
            temp_dict['approver1Email'] = ''
            if history_obj.approver1_id != None:
                user_id_list.append(str(history_obj.approver1.user_id))

            temp_dict['approver2']=str(history_obj.approver2.user_id) if history_obj.approver2_id!=None else ""
            temp_dict['approver2Email'] = ''
            if history_obj.approver2_id != None:
                user_id_list.append(str(history_obj.approver2.user_id))

            if history_obj.approver1_id != None and history_obj.approver_status in ("Rejected","Approved-1"):
                temp_dict['approval_1date'] = datetime.datetime.strftime(history_obj.approval_date, "%d-%m-%Y") if history_obj.approval_date!=None else ""

            if history_obj.approver2_id != None and history_obj.approver_status in ("Rejected","Approved"):
                temp_dict['approval_2date'] = datetime.datetime.strftime(history_obj.approval_date, "%d-%m-%Y") if history_obj.approval_date!=None else ""

            if Campaign_approver_obj:
                temp_dict['remainingBudget'] = Campaign_approver_obj.budget_allocated - Campaign_approver_obj.budget_used

            temp_dict['approver1Comment'] = history_obj.approver1_comment
            temp_dict['approver2Comment'] = history_obj.approver2_comment

            temp_dict["valueName"] = ""
            value_obj = None
            if history_obj.campaign_value != None:
                value_obj = history_obj.campaign_value.value
            if  value_obj!=None:
                temp_dict['valueName']=value_obj.name

            temp_dict["ecardTemplateName"] = ""
            temp_dict["ecardUrl"] = ""
            if history_obj.ecard!=None:
                ecard_obj = history_obj.ecard
                temp_dict['ecardTemplateName'] = ecard_obj.name
                temp_dict['ecardUrl'] = ecard_obj.background_image      

            temp_dict["receiever"] = ""
            temp_dict['receiverEmail'] = ''
            temp_dict['points_awarded'] = 0
            unit_campaign_transaction_objs = history_obj.unit_campaign_transaction
            for unit_campaign_transaction_obj in unit_campaign_transaction_objs:
                temp_2_dict = copy.deepcopy(temp_dict)
                temp_2_dict['receiever']=str(unit_campaign_transaction_obj.receiver_id)
                user_id_list.append(temp_2_dict['receiever'])
                temp_2_dict['points_awarded']=unit_campaign_transaction_obj.points
                history_csv.append(temp_2_dict)

        uuid_info_dict = get_user_info_from_user_id(ids[2], user_id_list)

        for i in range(0, len(history_csv)):
            if history_csv[i]["sender"] != "":
                sender_id = history_csv[i]["sender"]
                history_csv[i]["sender"] = uuid_info_dict.get(history_csv[i]["sender"],{}).get("fullName","")
                history_csv[i]['senderEmail'] = uuid_info_dict.get(sender_id,{}).get("email","")

            if history_csv[i]["approver1"] != "":
                approver1_id = history_csv[i]["approver1"]
                history_csv[i]["approver1"] = uuid_info_dict.get(history_csv[i]["approver1"],{}).get("fullName","")
                history_csv[i]['approver1Email'] = uuid_info_dict.get(approver1_id,{}).get("email","")
            
            if history_csv[i]["approver2"] != "":
                approver2_id = history_csv[i]["approver2"]
                history_csv[i]["approver2"] = uuid_info_dict.get(history_csv[i]["approver2"],{}).get("fullName","")
                history_csv[i]['approver2Email'] = uuid_info_dict.get(approver2_id,{}).get("email","")
            
            if history_csv[i]["receiever"] != "":
                receiver_id = history_csv[i]["receiever"]
                history_csv[i]["receiever"] = uuid_info_dict.get(history_csv[i]["receiever"],{}).get("fullName","")
                history_csv[i]['receiverEmail'] = uuid_info_dict.get(receiver_id,{}).get("email","")

        
        file_name = str(round(time.time() * 1000))+'.csv'
        file = os.getcwd() + "/files/" + file_name

        try:
            os.mkdir("files")
        except Exception as e:
            logger.warning("export_csv_campaign_history %s", str(e))

        with open(file, 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()


        file_url = upload_any_file(file, "text/csv")
        response["file_url"] = file_url
        response["status"] = 200
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("export_csv_campaign_history: %s at %s", e, str(exc_tb.tb_lineno))
        raise HTTPException(500)

    return  