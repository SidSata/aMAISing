
import wiringpi as  wp
wp.wiringPiSetupGpio()

wp.digitalWrite(20,1)
wp.digitalWrite(21,0)

key = cv2.waitKey(1) & 0xFF
if key == ord("q"):                                      # if the 'q' key is pressed, stop the loop
    break
