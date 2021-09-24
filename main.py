from tkinter import messagebox
import api
from tkinter import *


def submit():
    # Function for get location name.
    submit_btn['state'] = 'disabled'  #  Prevent multiplie requests.
    location_name = location_var.get()
    weather_information(location_name)


def weather_information(location):
    # Get all information about the weather and show in app.
    global icon_img
    weather = api.get_weather_info(location)
    # print(weather)
    if weather['cod'] == '404':
        messagebox.showerror('Error', "Location %s not found!" % location)
        exit()
    city_name = weather['name']
    country_code = weather['sys']['country']
    temperature = round(weather['main']['temp'])
    icon = weather['weather'][0]['icon']
    main_weather = weather['weather'][0]['main']
    description = weather['weather'][0]['description']
    feels_like = round(weather['main']['feels_like'])
    temp_min = round(weather['main']['temp_min'])
    temp_max = round(weather['main']['temp_max'])
    humidity = weather['main']['humidity']

    location_show = Label(root, text=city_name+', ' + country_code, font=('Verdana', 20))
    main_weather_show = Label(root, text=main_weather, font=('Verdana', 25))
    desc_show = Label(root, text='('+description+')', font=('Verdana', 12))
    temprature_show = Label(root, text=str(temperature)+"°", font=('Calibri', 75))
    temprature_max_show = Label(root, text=str(temp_max) + "°C", font=('Calibri', 15))
    temprature_min_show = Label(root, text=str(temp_min) + "°C", font=('Calibri', 15))
    sepa = Label(root, text="_____________", font=('Calibri', 5))
    main_weather_show.place(x=70, y=230)
    desc_show.place(x=200, y=240)
    temprature_show.place(x=70, y=270)
    temprature_max_show.place(x=270, y=300)
    temprature_min_show.place(x=270, y=340)
    sepa.place(x=270, y=325)
    location_show.place(x=15, y=180)

    image_url = "https://openweathermap.org/img/wn/"+icon+".png"
    api.download_icon(image_url)
    icon_img = PhotoImage(file='icon.png')
    icon_show = Label(root, image=icon_img, bg='#B3B3B3')
    icon_show.place(x=15, y=225)

    feels_like_show = Label(root, text='Feels like: ' + str(feels_like) + "°C", font=('Calibri', 15))
    feels_like_show.place(x=0, y=400)
    humdity_show = Label(root, text='Humidity: ' + str(humidity) + "%", font=('Calibri', 15))
    humdity_show.place(x=0, y=430)


# Window Settings
root = Tk()
root.geometry("400x500")
root.iconbitmap('sunrise.ico')
root.resizable(False, False)
img = PhotoImage(file='logo.png')
logo = Label(root, image=img)

root.title("Weather App")
location_var = StringVar()

enter_input_text = Label(root, text='Enter your location:', font=('Arial', 12))
location_entry = Entry(root, textvariable=location_var, font=('Arial', 12), justify='center')
submit_btn = Button(root, text='Submit', command=submit, width=10)


enter_input_text.grid(row=0, column=0)
location_entry.grid(row=0, column=1)
submit_btn.grid(row=0, column=2)
logo.place(x=0, y=30)

root.mainloop()


