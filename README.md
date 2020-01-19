# Automated Pill Management System
## Team aMAISing

* Manasi Rajan
* Meghna Gaddam
* Parth Behani
* Siddhant Satapathy
* Varun Agrawal

## Inspiration

**Theme :** Healthcare

One of the most pressing problems in medicine is the issue of medical non-adherence, where the patient deviates from the prescribed treatment regimen by failing to take prescribed doses of medication at allotted times. This often has severe consequences for both the patient and the healthcare system as a whole, as non-adherence leads to recurrence of illnesses, development of antibiotic resistance, ineffectiveness of drugs, and increased costs due to repeated hospitalization.

While there is already extensive research into methods to prevent medical non-adherence, particularly in the USA where non-adherence costs between $100 billion- $289 billion per year, we found a lack of practical on-the-ground solutions to address this problem in India. Non-adherence is most commonly seen among elderly or incapicitated patients living alone, and especially among people suffering from neuro-degenerative conditions such as dementia. Due to forgetfulness or incapability, it is difficult for them to consistently take medication at the required times without the assistance of a caregiver. 

In order to meet this urgent need, we developed an automated pill delivery and management system consisting of a robotic pill dispenser and a mobile app to enable patients and caregivers to accurately track medication according to a previously inputted schedule.

[Our presentation](https://github.com/SidSata/aMAISing/blob/master/Pill_Management_System_aMAISing.pdf)

## Technology

The Robot was designed using a Raspberry Pi 3B, DC and Servo Motors, Infrared Sensors, L293D Motor Drivers, Arduino and an LCD Display. Raspbian Jessie was used to program the robot. 

The app was implemented using MIT App Inventor.

(The app can be downloaded from [here](https://github.com/SidSata/aMAISing/blob/master/App.aia) and can be opened on MIT App Inventor by clicking My Projects -> Import project (.aia) from my computer -> Uploading the downloaded file)

The Pill Management App allows the user to enter up to four medications (corresponding to 4 slots on the robot), along with the respective times at which they are to be taken and the slot number on the robot.

At the allotted time, the app displays an alert on the mobile phone (appearing as a pop-up) and communicates a signal to the robot via a bluetooth module. The robot begins traveling towards the patient using the bluetooth location and uses infrared sensors to avoid obstacles. The pill dispenser arm of the robot rotates towards the desired pill slots using servo motors, and the type of medicine and time is displayed to the patient via an Arduino LCD display (not integrated into the current prototype due to restrictions on weight).

[Application UI](https://github.com/SidSata/aMAISing/blob/master/Application_UI.png)

Live demonstrations:

[Movement and rotation of robot](https://github.com/SidSata/aMAISing/blob/master/IMG_1935.MOV)

[Obstacle detection and avoidance](https://github.com/SidSata/aMAISing/blob/master/IMG_1940.MOV)


## Feasibility

The robot is easily reproducable, and the mobile app is free to use and can function independently of the robot. We see two major applications of this system-

1.  Acting as a vital companion to elderly/incapacitated persons, who often live alone at home and do not have regular access to a caregiver, and as a result often forget to take their required medications on time. The patient could input their medication schedule once, and get the required medication delivered to them at the given time, therefore making them more self-reliant. The system could also be used by the caregiver to better track the medication of the patient.

2.  Mass deployment in hospitals and other healthcare centers, where they can be utilized by doctors and nurses to easily track the medication schedules of hundreds of patients and automatically deliver the required pills.

## Further developments

* This system only incorporates pills. A logical next step would be to deliver other types of medication, such as syrups and sprays.

* Dispensing specific dosages of pills. We are aware that a significant part of non-adherence constitutes taking appropriate dosages, and that our prototype fails to completely achieve this goal. To this end, we propose the use of a rotating drum mechanism, which dispenses one pill at a time until the required dosage is attained.

* Optimized indoor mapping using SONAR based platforms to enhance accuracy and efficiency.

* Tracking non-adherence, such as when a patient does not take a pill at the required time, and alerting emergency contacts.

* Better integration between the mobile app and the robot.

