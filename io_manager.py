# FILE CURRENTLY BROKEN, PLEASE DON'T USE IT

def io_manager():

    if platform == "esp8266":
        gpioCheck = [0, 2, 4, 5, 11, 12, 13, 14, 15, 16]
    else:
        print(platform + " platform not supported!")
        main()

    head = ["IO Manager",
            "Platform: ",platform,
            "GPIO: ",str(len(gpioCheck)),
            "",""]
    body = code("Recent Activity: ", ioLog)
    tail = ["Configure GPIO","Set GPIO","",
            "","","",
            "","","",
            "Return","",""]

    screen(head,body,tail)
    options = get_input()

    while True:
        if options == '0':  # RETURN
            main()

        if options == '7':  # READ GPIO
            gpio = input("Enter a GPIO number: ")
            if int(gpio) != any(gpioCheck):
                print("GPIO" + gpio) + " not available"
                io_manager()
            ioLog.append("GPIO" + gpio + "current value = " +
            Pin(int(gpio), Pin.IN).value())
            io_manager()

        if options == '8':  # SET GPIO
            gpio = input("Enter a GPIO number: ")
            if int(gpio) != any(gpioCheck):
                print("GPIO" + gpio) + " not available"
                io_manager()
            state = input("[1] ON [0] OFF")
            if state:
                Pin(int(gpio), Pin.OUT).on()
                ioLog.append("GPIO" + gpio + " now set on")
            else:
                Pin(int(gpio), Pin.OUT).off()
                ioLog.append("GPIO" + gpio + " now set off")
            io_manager()

        else:
            get_input()