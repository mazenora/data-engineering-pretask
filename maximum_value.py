from itertools import combinations

def maximum_value(orders: list, maximum_weight: int) -> int:
    """
        A Function to Return Best Maximum Value from A List of Orders 
        Based on its Maximum Weight Criteria, Through finding all possible 
        combinations of them.

        :param orders: a list of orders
        :type orders: list
        :param maximum_weight: the maximum allowd weight
        :type maximum_weight: int
    """
    # Check if there is any orders.
    if orders:
        # Check if there is only one order.
        if len(orders) == 1:
            # Return 0 if Order's weight is more than the maximum weight otherwise return the Order's value.
            return 0 if orders[0]["weight"] > maximum_weight else orders[0]["value"] 
        else:
            # Define inital best value to return as Zero
            best_maximum_value = 0

            # Define Get Best Value Inner Function:
            def get_best_maximum_value(orders_list: list,best_maximum_value: int,maximum_weight: int) -> int:
                """
                    An Inner Function to Return Best Maximum Value From a List of Orders 
                    Based on its Maximum Weight Criteria.
                    
                    :param orders_list: a list of orders
                    :type orders_list: list
                    :param best_maximum_value: best sum of values to return
                    :type best_maximum_value: int
                    :param maximum_weight: the maximum allowd weight 
                    :type maximum_weight: int

                """
                sum_weight =  sum_value = 0
                for orders in orders_list:
                    if isinstance(orders, dict):
                        sum_weight += orders["weight"]
                        sum_value += orders["value"]
                    else:
                        # Recursive Call for Each Set of Orders. 
                        best_maximum_value = get_best_maximum_value(orders,best_maximum_value,maximum_weight)
                if (sum_weight <=  maximum_weight) and (sum_value > best_maximum_value):
                    best_maximum_value = sum_value               
                return best_maximum_value
            
            # Get Best Value for all orders in the List (Sum of all weights and values):
            best_maximum_value = get_best_maximum_value(orders, best_maximum_value, maximum_weight)
            # If Best Value is positive then return it.  
            if best_maximum_value > 0 :
                return best_maximum_value
            else:
                # Let's get all possible combinations of our orders and Get the Best Value.
                for i in range(1,len(orders)):
                    # Generate List of combinations.
                    combination_list = list(combinations(orders,i))
                    # Get Best value for List of combinations.
                    best_maximum_value = get_best_maximum_value(combination_list, best_maximum_value, maximum_weight)
            return best_maximum_value        
    else:
        return 0
