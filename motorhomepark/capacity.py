# def check_booking_dates(start_date, end_date):
#     status = 0
#     print(f'The function was called.... with {start_date} and {end_date}')
#     date_object = datetime.strptime(start_date, '%m/%d/%Y').date()
#     date_object2 = datetime.strptime(end_date, '%m/%d/%Y').date()
#     date_object.strftime('%m/%d/%Y')
#     date_object2.strftime('%m/%d/%Y')    
#     # confirm the dates are correct,
#     print(f'After processing to date objects .... with {date_object} and {date_object2}')
#     check_list = SiteCapacity.objects.all()

#     # loop through the dates
#     delta = date_object2 - date_object
#     print('Delta is ',delta)
#     for i in range(delta.days):
#         myDay = date_object + timedelta(days=i) # this is correct number of days
#         site_capacity = check_list.get(booking_date=myDay)
#         if site_capacity.booking_date in check_list:
#             if settings.GLOBAL_SETTINGS.CAPACITY > (site_capacity.slots_used + 1):
#                 status = 0               
#         else: 
#             status = 1

#     return status  
#     print(f'Date: {site_capacity}, space used :{space_used}')

        #for check in check_list:
        #print('loop running')
        # if (check.booking_date is None):
        #     print(f'No booking for {check.booking_date}')
        # else:
        #     print(f'{check.booking_date} slots used {check.slots_used}')


    


    
