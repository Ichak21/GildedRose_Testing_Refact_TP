# -*- coding: utf-8

import numbers

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name == "Aged Brie":
                if item.sell_in < 0 and item.quality<49:
                    item.quality += 2
                elif item.sell_in > 0 and item.quality<50:
                    item.quality += 1
                item.sell_in -= 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in<6 and item.sell_in>0 and item.quality<50:
                    item.quality += 3
                elif item.sell_in<11 and item.sell_in>=6 and item.quality<50:
                    item.quality += 2
                elif item.sell_in >0 and item.quality<50:
                    item.quality += 1
                elif item.sell_in <= 0:
                    item.quality=0
                item.sell_in -= 1
            
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.quality=80

            else:
                if item.sell_in<0 and item.quality >1:
                    item.quality -= 2
                elif item.quality>0:
                    item.quality -= 1
                item.sell_in -= 1


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
