from TrafficData import TrafficData

d = TrafficData()
d.read('../traffic_data.txt')
d.split()
d.train()
d.regres()
d.test()
d.predict()