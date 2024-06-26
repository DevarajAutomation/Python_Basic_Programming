import requests

class Weather:

    def __init__(self,name,lat,lon,units="metric"):
        self.name=name
        self.lat=lat
        self.lon=lon
        self.units=units
        self.get_data()

    def get_data(self):
        
        try:
            self.response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=23e034b53ae92a5037f7c07fd16ecc69")

        except:
            print('Internet connection is required!')

    
    def post_data(self):
        self.unit_of_measure='°C'
        
        json_response=self.response.json()
        self.name=json_response['name']
        self.temp=json_response['main']['temp']
        self.temp_min=json_response['main']['temp_min']
        self.temp_max=json_response['main']['temp_max']
        print(f"The temparature in {self.name} is {self.temp}{self.unit_of_measure}")
        print(f"The minimum temparature in {self.name} is {self.temp_min}{self.unit_of_measure}")
        print(f"The maximum temparature in {self.name} is {self.temp_max}{self.unit_of_measure}")
        self.cities=dict([(self.name,self.temp)])

        #self.cities['name']=self.name
        #self.cities['temparature']=self.temp,self.unit_of_measure
        print(self.cities)
weather_1=Weather('BLR',12.97194000,77.59369000)
weather_2=Weather('TMK',13.50000000,77.00000000)
weather_3=Weather('CHN',13.08784000,80.27847000 )
weather_1.post_data()
weather_2.post_data()
weather_3.post_data()

