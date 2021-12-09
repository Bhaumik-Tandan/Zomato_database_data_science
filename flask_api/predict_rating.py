from collections import OrderedDict
from numpy import array
def predict_rating(modal,data,cuisines):
    fields_dict = OrderedDict()

    fields_dict['longitude'] = data.get('longitude')
    fields_dict['latitude'] = data.get('latitude')
    fields_dict['average_cost_for_two'] = data.get('average_cost_for_two')
    fields_dict['has_table_booking'] = data.get('has_table_booking')
    fields_dict['has_online_delivery'] = data.get('has_online_delivery')
    fields_dict['is_delivering_now'] = data.get('is_delivering_now')
    fields_dict['switch_to_order_menu'] = data.get('switch_to_order_menu')
    fields_dict['price_range'] = data.get('price_range')
    fields_dict['votes'] = data.get('votes')

    for k,v in fields_dict.items():
        if v is None:
            fields_dict[k] = 0

    cuisines_dict=OrderedDict(zip(cuisines,len(cuisines)*[0]))
    for i in data["cuisines"]:
        cuisines_dict[i]=1

    model_fields = list(fields_dict.values())+list(cuisines_dict.values())

    return modal.predict(array([model_fields]))
    