from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()
mc.postToChat("Injected simpleclient beta 1.0")
mc.postToChat("we are not assosiated with mojang or microsoft any way")
while True:
    pos = mc.player.getTilePos()
    mc.getBlock(pos.x, pos.y, pos.z) != 1
    mc.setBlock(pos.x, pos.y-1, pos.z, 1)
while True: 
    pos = mc.player.getTilePos()
    mc.getBlock(pos.x, pos.y, pos.z) != 95
    mc.setBlock(pos.x, pos.y-1, pos.z, 95)
    mc.setBlock(pos.x-1, pos.y-2, pos.z-1, 0)
    mc.setBlock(pos.x+1, pos.y+1, pos.z+1, 0)