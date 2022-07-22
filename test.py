# --------------------------------------------------------------------------------------------------
##Tried to get keys from one yaml file but getting only high level keys

# import yaml
#
# with open('dummy_yaml.yaml') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     print(data)
#
# abc=data.keys()
# print(abc)


# ---------------------------------------------------------------------------------------------------

import yaml
from deepdiff import DeepDiff


def yaml_as_dict(my_file):
    my_dict = {}
    with open(my_file, 'r') as fp:
        docs = yaml.safe_load_all(fp)
        for doc in docs:
            for key, value in doc.items():
                my_dict[key] = value
    return my_dict


if __name__ == '__main__':
    a = yaml_as_dict('dummy_yaml1.yaml')
    b = yaml_as_dict('dummy_yaml2.yaml')
    ddiff = DeepDiff(a, b, ignore_order=True)
    print(ddiff)
