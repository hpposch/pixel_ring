"""
LED pattern like Echo
"""

import time


class Echo(object):
    brightness = 24 * 8

    def __init__(self, show, number=12):
        self.pixels_number = number
        self.pixels = [0] * 4 * number

        if not callable(show):
            raise ValueError('show parameter is not callable')

        self.show = show
        self.stop = False

    def wakeup(self, direction=0):
        position = int((direction + 15) / (360 / self.pixels_number)) % self.pixels_number

        pixels = [0, 0, 0, self.brightness] * self.pixels_number
        pixels[position * 4 + 2] = self.brightness

        self.show(pixels)

    def listen(self):
        pixels = [0, 0, 0, self.brightness] * self.pixels_number

        self.show(pixels)

    def think(self):
        half_brightness = int(self.brightness / 2)
        pixels  = [0, 0, half_brightness, half_brightness, 0, 0, 0, self.brightness] * self.pixels_number

        while not self.stop:
            self.show(pixels)
            time.sleep(0.2)
            pixels = pixels[-4:] + pixels[:-4]

    def speak(self):
        step = int(self.brightness / 12)
        position = int(self.brightness / 2)
        while not self.stop:
            pixels  = [0, 0, position, self.brightness - position] * self.pixels_number
            self.show(pixels)
            time.sleep(0.01)
            if position <= 0:
                step = int(self.brightness / 12)
                time.sleep(0.4)
            elif position >= int(self.brightness / 2):
                step = - int(self.brightness / 12)
                time.sleep(0.4)

            position += step

    def off(self):
        self.show([0] * 4 * 12)

    def error(self):
        pixels = []
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.show(pixels)

class GoogleHome(object):
    def __init__(self, show):
        self.basis = [0] * 4 * 12
        self.basis[0 * 4 + 1] = 8
        self.basis[3 * 4 + 1] = 4
        self.basis[3 * 4 + 2] = 4
        self.basis[6 * 4 + 2] = 8
        self.basis[9 * 4 + 3] = 8

        self.pixels = self.basis

        if not callable(show):
            raise ValueError('show parameter is not callable')

        self.show = show
        self.stop = False

    def wakeup(self, direction=0):
        position = int((direction + 90 + 15) / 30) % 12

        basis = self.basis[position*-4:] + self.basis[:position*-4]
        
        pixels = [v * 25 for v in basis]
        self.show(pixels)
        time.sleep(0.1)

        pixels =  pixels[-4:] + pixels[:-4]
        self.show(pixels)
        time.sleep(0.1)

        for i in range(2):
            new_pixels = pixels[-4:] + pixels[:-4]
            
            self.show([v/2+pixels[index] for index, v in enumerate(new_pixels)])
            pixels = new_pixels
            time.sleep(0.1)

        self.show(pixels)
        self.pixels = pixels

    def listen(self):
        pixels = self.pixels
        for i in range(1, 25):
            self.show([(v * i / 24) for v in pixels])
            time.sleep(0.01)

    def think(self):
        pixels = self.pixels

        while not self.stop:
            pixels = pixels[-4:] + pixels[:-4]
            self.show(pixels)
            time.sleep(0.2)

        t = 0.1
        for i in range(0, 5):
            pixels = pixels[-4:] + pixels[:-4]
            self.show([(v * (4 - i) / 4) for v in pixels])
            time.sleep(t)
            t /= 2

        self.pixels = pixels

    def speak(self):
        pixels = self.pixels
        step = 1
        brightness = 5
        while not self.stop:
            self.show([(v * brightness / 24) for v in pixels])
            time.sleep(0.02)

            if brightness <= 5:
                step = 1
                time.sleep(0.4)
            elif brightness >= 24:
                step = -1
                time.sleep(0.4)

            brightness += step

    def off(self):
        self.show([0] * 4 * 12)

    def error(self):
        pixels = []
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.show(pixels)

class Smartlife(object):
    brightness = 24 * 8

    def __init__(self, show, number=12):
        self.pixels_number = number
        #self.pixels = [0] * 8 * number

        if not callable(show):
            raise ValueError('show parameter is not callable')

        self.show = show
        self.stop = False

    def wakeup(self, direction=0):

        pixels = []

        k = 200
        for k in range(255):
            j = 1
            k += 50
            if k > 255:
                break

            for j in range(12):
                self.add_pixel(pixels, 0, 0, k, 0)
                continue
            self.show(pixels)
            time.sleep(0.000001)
            pixels = []
            continue

    def listen(self):

        while not self.stop:
            pixels = []
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.show(pixels)
            time.sleep(0.2)

            pixels = []
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.show(pixels)
            time.sleep(0.2)

    def think(self):

        while not self.stop:
            pixels = []
            loopTime = 0.03

            i = 0
            j = 0
            k = 0
            count = 1
            for k in range(12):
                for j in range(count):
                    self.add_pixel(pixels, 0, 0, 255, 0)
                    j += 1
                    continue
                for i in range(12 - count):
                    self.add_pixel(pixels, 0, 0, 0, 0)
                    i += 1
                    continue

                self.show(pixels)
                time.sleep(loopTime)
                pixels = []
                j = 0
                count += 1
                continue

            pixels = []
            i = 0
            j = 0
            k = 0
            count = 1
            for k in range(12):
                for j in range(count):
                    self.add_pixel(pixels, 0, 0, 0, 0)
                    j += 1
                    continue
                for i in range(12 - count):
                    self.add_pixel(pixels, 0, 0, 255, 0)
                    i += 1
                    continue

                self.show(pixels)
                time.sleep(loopTime)
                pixels = []
                j = 0
                count += 1
                continue

    def speak(self):
        while not self.stop:
            pixels = []
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.add_pixel(pixels, 0, 0, 255, 0)
            self.show(pixels)
            time.sleep(0.45)

            pixels = []
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.add_pixel(pixels, 0, 0, 180, 50)
            self.show(pixels)
            time.sleep(0.45)

    def off(self):
        self.show([0] * 4 * 12)

    def error(self):
        pixels = []
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.add_pixel(pixels, 0, 255, 0, 0)
        self.show(pixels)


    def add_pixel(self, pixels, dontKnow, r, g, b):
        pixels.append(dontKnow)
        pixels.append(r)
        pixels.append(g)
        pixels.append(b)

    def set_all_pixles(self, pixels, dontKnow, r, g, b):
        i = 1
        for i in range(12):
            pixels.append(dontKnow)
            pixels.append(r)
            pixels.append(g)
            pixels.append(b)
