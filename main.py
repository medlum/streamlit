
from api_call import api_func
from data_proc import data_proc_func
from stream_map import map_stream_func

def main():

    nowplus8, data = api_func()
    complete_list = data_proc_func(data)
    map_stream_func(complete_list)


if __name__ == "__main__":
    main()
