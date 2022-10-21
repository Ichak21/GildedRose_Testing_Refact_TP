import unittest
from gilded_rose import Item, GildedRose

def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name

def test_îtems_is_empty():
    items_to_test = []
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test == []

def test_if_dlc_out_quality_recrease_twice():
    items_to_test = [Item("not_Aged_Brie_Or_Concert_Ticket_or_Sulfuras",-1,10)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 10-2

def test_qulity_never_should_be_negative():
    items_to_test = [Item("not_Aged_Brie_Or_Concert_Ticket_or_Sulfuras",0,0),Item("not_Aged_Brie_Or_Concert_Ticket_or_Sulfuras",-2,0)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 0
    assert items_to_test[1].quality == 0

def test_quality_never_over_50():
    items_to_test = [Item("Aged Brie",-1,50),Item("Backstage passes to a TAFKAL80ETC concert",1,50)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 50
    assert items_to_test[1].quality == 50

def test_quality_of_aged_brie_increase():
    items_to_test = [Item("Aged Brie",5,40)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 41

def test_quality_of_aged_brie_increase():
    items_to_test = [Item("Aged Brie",5,40)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 41

def test_sulfuras_never_move_for_sellIn():
    items_to_test = [Item("Sulfuras, Hand of Ragnaros",30,40)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].sell_in == 30

def test_sulfuras_never_move_for_qulity():
    items_to_test = [Item("Sulfuras, Hand of Ragnaros",30,80)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 80

def test_for_backstage_passes_quality_up_by_2_when_dlc_10to5():
    items_to_test = [Item("Backstage passes to a TAFKAL80ETC concert",9,40)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 42

def test_for_backstage_passes_quality_up_by_3_when_dlc_5to0():
    items_to_test = [Item("Backstage passes to a TAFKAL80ETC concert",3,40)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 43

def test_for_backstage_passes_quality_drop_to_0_after_the_concert():
    items_to_test = [Item("Backstage passes to a TAFKAL80ETC concert",0,40)]
    gilded_rose_to_test = GildedRose(items_to_test)
    gilded_rose_to_test.update_quality()
    assert items_to_test[0].quality == 0

