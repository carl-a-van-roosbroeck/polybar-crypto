# polybar-crypto
A *polybar script* that displays the price or percentage change of various **crypto-currencies**.



![screen](https://user-images.githubusercontent.com/24377188/31326832-34dd06de-ad27-11e7-908f-9e7d72398eb7.jpg)



# Setup
```
git clone https://github.com/carl-a-van-roosbroeck/polybar-crypto &&
    cd polybar-crypto &&
    mkdir -p ~/.config/polybar &&
    cp ./{crypto-config,crypto.py} ~/.config/polybar &&
    sudo chmod u+x ~/.config/polybar/crypto.py
```

Then in `~/.config/polybar/config`:

```
[bar/top]

...

modules-left = crypto

...

[module/crypto]
type = custom/script
interval = 300
exec = /home/<user>/.config/polybar/crypto.py

```

## Dependencies
The [cryptocoins](https://github.com/allienworks/cryptocoins) *icon font* is used in the screenshots, though you are free to use any other font.

If using the **cryptocoins** icon font, ensure that the following line is present in your `~/.config/polybar/config`:

```
[bar/top]

...

font-2 = cryptocoins:style=Regular;0
```

# Example Configuration

`~/.config/polybar/crypto-config`
```
[general]
base_currency = EUR
display = percentage
round = 3

[bitcoin]
icon = 
color = #f2a900

[ethereum]
icon = 
color = #3c3c3d

[monero]
icon = 
color = #ff6600
```

## Display Modes

`display = price`

![screen](https://user-images.githubusercontent.com/24377188/31331319-4ef14406-ad3e-11e7-9242-12440ef96774.jpg)

`display = percentage`

![screen](https://user-images.githubusercontent.com/24377188/31331342-65e40428-ad3e-11e7-88e0-3b87921805c7.jpg)

`display = both`

![screen](https://user-images.githubusercontent.com/24377188/31331368-80faac76-ad3e-11e7-9977-e86b1eebe401.jpg)

## Rounding

`round = 0` No rounding
`round = {n}`Round

## Color

`color = {hex color}` Set the color of the symbol

