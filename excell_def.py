def send_to_r(r_name,list_of_parameters):
    #print("router name=",r_name)
    #print("ip=", list_of_parameters[0])
    #print("mask=", list_of_parameters[1])
    #print("int name=",list_of_parameters[2])
    interface="interface"+list_of_parameters[2]
    ip="ip address "+list_of_parameters[0]+" subnetmask "+list_of_parameters[1]

    print(r_name)
    print(interface)
    print(ip)