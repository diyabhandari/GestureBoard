from virtual_mouse import virtual_mouse
from volume import volume_control
def main():
  virtual_mouse()
  volume_control()
  #opens twice, first runs for virtual mouse, then ig it opens for the next
  #we dont want cam opening again and again for each feature, merge similar lines of code, that deal with making an object of the camera
if __name__ == "__main__":
  main()