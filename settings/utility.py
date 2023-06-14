def _convert(list_convert):
    '''
    набор идентификаторов товаров трансформируется
    из такого представления - [(5,),(8,),...] в такое [5, 8,...]
    '''
    return [itm[0] for itm in list_convert]


def total_cost(list_quantity, list_price):
    order_total_cost = 0
    for ind, itm in enumerate(list_price):
        order_total_cost += list_quantity[ind] * list_price[ind]
        return order_total_cost


def total_quantity(list_quantity):
    order_total_quantity = 0
    for itm in list_quantity:
        order_total_quantity += itm
        return order_total_quantity


def get_total_cost(DB):
    '''
    :return: общая стоимость товара
    '''
    all_product_id = DB.select_all_product_id()
    all_price = [DB.select_single_product_price(itm) for itm in all_product_id]
    all_quantity = [DB.select_order_quantity(itm) for itm in all_product_id]
    return total_cost(all_quantity, all_price)


def get_total_quantity(DB):
    '''
    :return: общее количество заказанной единицы товара
    '''
    all_product_id = DB.select_all_product_id()
    all_quantity = [DB.select_order_quantity(itm) for itm in all_product_id]
    return total_quantity(all_quantity)
