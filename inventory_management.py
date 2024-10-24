# inventory_management.py

#TASK 1: Calculate the average demand and max demand based on historical data. Print the average demand.
    
#List of historical demand values:
historical_demand = [100, 120, 80, 90, 110]
total_demand = 0
for num in historical_demand:
  total_demand=total_demand+num
print("total_demand:",total_demand)
avg_demand=total_demand/len(historical_demand)
print("average demand:",avg_demand)
print("Max_demand:",max(historical_demand))

#PRINT HERE YOUR RESULT
total_demand: 500
average demand: 100.0
Max_demand: 120


#TASK 2:Calculate the average lead time and max lead time based on previous orders.
order_data = [
            {'order_date': '2023-01-01', 'delivery_date': '2023-01-05'},
            {'order_date': '2023-01-10', 'delivery_date': '2023-01-13'},
            {'order_date': '2023-01-20', 'delivery_date': '2023-01-25'}
        ]

#PRINT HERE YOUR RESULT

"""
#TASK 3:Calculate the safety stock based on average demand, lead time, and desired service level based on the following formula:
#Safety stock = (maximum daily sales x maximum lead time) – (average daily sales x average lead time)

average_demand = #Result of TASK 1
max_demand = #Result of TASK 1
average_lead_time = #Result of TASK 2
max_lead_time = #Result of TASK 2
"""

#PRINT HERE YOUR RESULT

def calculate_reorder_point(average_demand, lead_time, safety_stock):
    #TASK 4: Calculate the reorder point based on average demand, lead time, and safety stock in this function and return its value. 
    #Reorder point = Average Lead Time*Average Demand + Safety Stock
    """"

    :param average_demand: Average demand per day
    :param lead_time: Average lead time in days
    :param safety_stock: Calculated safety stock
    :return: Reorder point quantity
    """
    pass

#TASK 5: Call the function with the average_demand of TASK 1, average lead time of TASK 2, and safety stock of TASK 3.

def optimize_reorder_point(historical_demand, order_data, holding_cost, stockout_cost):

    #TASK 6: Optimize the reorder level based on historical data and cost factors for this function. Use the previous tasks but do not assume the given data.

    """
    :param historical_demand: List of historical demand values
    :param order_data: List of dictionaries containing order and delivery dates 
    :return: Optimal reorder point
    """
    pass

#TASK 7: Call the function with the following data:
order_data = [
            {'order_date': '2023-01-01', 'delivery_date': '2023-01-08'},
            {'order_date': '2023-01-08', 'delivery_date': '2023-01-13'},
            {'order_date': '2023-01-14', 'delivery_date': '2023-01-25'}
        ]
historical_demand = [200, 220, 380, 190, 210]
