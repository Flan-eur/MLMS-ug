/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - migrant1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`migrant1` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `migrant1`;

/*Table structure for table `accommodation` */

DROP TABLE IF EXISTS `accommodation`;

CREATE TABLE `accommodation` (
  `Accommod_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Agent_Id` int(11) NOT NULL,
  `Labour_Id` int(11) NOT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `Latitude` bigint(20) DEFAULT NULL,
  `Longitude` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`Accommod_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `accommodation` */

insert  into `accommodation`(`Accommod_Id`,`Agent_Id`,`Labour_Id`,`Place`,`Post`,`pin`,`Latitude`,`Longitude`) values (1,2,4,'fsdg','ewdsg',3,10,76),(2,2,10,'dvv','xcb',0,10,76),(3,2,4,'kdvanthra','kottyam',567582,1000,1),(4,2,4,'pala','kannavam',670678,1000,1);

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `account_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_no` varchar(50) DEFAULT NULL,
  `ifsc_code` varchar(50) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `account` */

insert  into `account`(`account_id`,`account_no`,`ifsc_code`,`balance`,`user_id`) values (1,'452500123652','nvy2525',4000,13),(2,'234','222',4000,2),(3,'454248110002565','nvm2525',69031,20),(4,'45252547878963','nvm2558',67223,24),(6,'4548750006598','synb0025',7390,25),(7,'4755589006565','025',20000,15);

/*Table structure for table `agentreg` */

DROP TABLE IF EXISTS `agentreg`;

CREATE TABLE `agentreg` (
  `Login_id` int(11) NOT NULL,
  `Agent_Name` varchar(50) DEFAULT NULL,
  `Agent_Place` varchar(20) DEFAULT NULL,
  `Agent_Post` varchar(20) DEFAULT NULL,
  `Agent_Pin` int(11) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `District` varchar(20) DEFAULT NULL,
  `Phone_no` bigint(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `Agent_Licence no` bigint(20) DEFAULT NULL,
  `Licence_Image` varchar(200) DEFAULT NULL,
  `Government_Id` varchar(20) DEFAULT NULL,
  `Id_no` int(11) DEFAULT NULL,
  `Id_Image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `agentreg` */

insert  into `agentreg`(`Login_id`,`Agent_Name`,`Agent_Place`,`Agent_Post`,`Agent_Pin`,`Age`,`DOB`,`Gender`,`District`,`Phone_no`,`Email`,`Agent_Licence no`,`Licence_Image`,`Government_Id`,`Id_no`,`Id_Image`) values (2,'sudhakaran','paral','paral',670671,50,'2020-05-06','male','kannur',6154648412,'dufukuiydy',3265651,'/static/mphoto/070221-140304.jpg','aadaar',265,'/static/mphoto/180421-095934.jpg'),(7,'babu','paral','paral',670671,56,'0000-00-00','male','Kasargod',9947262113,'susu@gmail.com',6788686,'/static/mphoto/070221-140304.jpg','aadhaar',78990,'/static/mphoto/070221-140304.jpg'),(15,'Ravi','paral','paral',670671,50,'0000-00-00','male','Kozhikode',34675858765,'ravi@gmail.com',5446778,'/static/mphoto/230321-112038.jpg','Aadhaar',1234567876,'/static/mphoto/230321-112038.jpg'),(16,'varun','kpba','kpba',670643,20,'0000-00-00','male','Kannur',9961033242,'varun@gmail.com',123456,'/static/mphoto/230321-114857.jpg','adhar',20402,'/static/mphoto/230321-114857.jpg'),(17,'vr','kk','hjj',233,52,'0000-00-00','male','Wayanad',6985675896,'var@gmail.com',458,'/static/mphoto/230321-115444.jpg','adhr',20403,'/static/mphoto/230321-115444.jpg'),(20,'riyas','pala','pala',670650,56,'1993-05-06','male','Kottayam',8689874565,'riyas@gmail.com',654897,'/static/mphoto/180421-095934.jpg','pan card',256895353,'/static/mphoto/180421-095934.jpg'),(24,'shafi','palarivattam','palarivattam',651750,43,'1977-02-06','male','Ernakulam',8689874565,'shafi@gmail.com',6356565854,'/static/mphoto/060521-091503.jpg','pan card',25254565,'/static/mphoto/060521-091503.jpg');

/*Table structure for table `apayment` */

DROP TABLE IF EXISTS `apayment`;

CREATE TABLE `apayment` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `agentid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `amt` float DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `apayment` */

insert  into `apayment`(`pid`,`agentid`,`cid`,`amt`,`date`) values (1,2,13,500,'2021-03-28');

/*Table structure for table `assignjob` */

DROP TABLE IF EXISTS `assignjob`;

CREATE TABLE `assignjob` (
  `Job_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Agent_Id` int(11) NOT NULL,
  `Labour_Id` int(11) NOT NULL,
  `Works` varchar(100) DEFAULT NULL,
  `Work_days` bigint(20) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Work_date` varchar(20) DEFAULT NULL,
  `Work_time` time DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`Job_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `assignjob` */

insert  into `assignjob`(`Job_Id`,`Agent_Id`,`Labour_Id`,`Works`,`Work_days`,`Place`,`Work_date`,`Work_time`,`latitude`,`longitude`) values (3,2,4,'vhjvdschz',NULL,'gsfhfx','12:','00:00:10',NULL,NULL),(4,2,10,'vaarp',NULL,'kannavam','10:12:2020','10:45:00',NULL,NULL),(5,2,4,'yeusfou',NULL,'efwg','10:12:2021','09:30:00',NULL,NULL),(6,2,4,'thepp',NULL,'kdvanthra','2021-04-06','02:46:00',NULL,NULL),(7,2,4,'theioo',NULL,'kannavm','2021-04-14','16:50:00',NULL,NULL),(8,2,4,'vaarp',15,'kdvanthra','2021-04-27','07:20:00',NULL,NULL),(9,2,10,'paint',NULL,'kannavm','2021-04-26','10:47:00',20000,10000),(10,2,10,'thepp',4,'pala','2021-05-03','07:33:00',1000,10000),(11,2,4,'thepp',12,'pala','2021-05-03','06:39:00',856666,454545);

/*Table structure for table `cfeedback` */

DROP TABLE IF EXISTS `cfeedback`;

CREATE TABLE `cfeedback` (
  `Feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `Customer_id` int(11) NOT NULL,
  `Feedback` varchar(50) DEFAULT NULL,
  `feedback_date` datetime DEFAULT NULL,
  PRIMARY KEY (`Feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `cfeedback` */

insert  into `cfeedback`(`Feedback_id`,`Customer_id`,`Feedback`,`feedback_date`) values (1,5,'rfsdgrdh','2021-02-02 12:20:56'),(2,12,'','2021-03-20 00:00:00'),(3,12,'fghjkfghjk','2021-03-20 00:00:00'),(4,12,'abcde','2021-03-20 00:00:00'),(5,22,'egfyuwetifuytriufterug','2021-04-18 00:00:00'),(6,22,'egfyuwetifuytriufterug','2021-04-18 00:00:00');

/*Table structure for table `companyreg` */

DROP TABLE IF EXISTS `companyreg`;

CREATE TABLE `companyreg` (
  `Login_Id` int(11) NOT NULL,
  `Company_name` varchar(20) DEFAULT NULL,
  `Company_place` varchar(20) DEFAULT NULL,
  `Company_post` varchar(20) DEFAULT NULL,
  `Company_pin` int(11) DEFAULT NULL,
  `District` varchar(20) DEFAULT NULL,
  `Phone_no` bigint(20) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Licence_no` int(11) DEFAULT NULL,
  `Licence_image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Login_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `companyreg` */

insert  into `companyreg`(`Login_Id`,`Company_name`,`Company_place`,`Company_post`,`Company_pin`,`District`,`Phone_no`,`Email`,`Licence_no`,`Licence_image`) values (6,'lic','efghth','hrthrt',NULL,'kasargod',8897456233,'lic@gmail.com',NULL,'/static/mphoto/180421-101857.jpg'),(13,'jeevan jyothi','malur','malur',4466787,'kannur',63475687553,'jeevan@gmail.com',56762,'/static/mphoto/210321-103303.jpg'),(14,'','','',0,'kannur',0,'',0,'/static/mphoto/210321-103534.jpg'),(23,'js','pala','pala',670650,'Kannur',8848736477,'js@gmail.com',2147483647,'/static/mphoto/180421-101857.jpg'),(25,'hdf','kannur','kannur',670678,'Kannur',8935454657,'hdf1@gmail.com',2147483647,'/static/mphoto/080521-120139.jpg');

/*Table structure for table `customerreg` */

DROP TABLE IF EXISTS `customerreg`;

CREATE TABLE `customerreg` (
  `Login_Id` int(11) NOT NULL,
  `Customer_name` varchar(20) DEFAULT NULL,
  `Customer_place` varchar(20) DEFAULT NULL,
  `Customer_post` varchar(20) DEFAULT NULL,
  `Customer_pin` int(11) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Phone_no` bigint(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `Id_proof` varchar(50) DEFAULT NULL,
  `Id_no` int(11) DEFAULT NULL,
  `Id_image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Login_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `customerreg` */

insert  into `customerreg`(`Login_Id`,`Customer_name`,`Customer_place`,`Customer_post`,`Customer_pin`,`Age`,`DOB`,`Gender`,`Phone_no`,`Email`,`Id_proof`,`Id_no`,`Id_image`) values (5,'varun','paral','dhck',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(22,'aswin','malur','malur',670678,28,'1998-12-06','male',8086032445,'aswin@gmail.com','PAN Card',2345678,'/static/mphoto/180421-101735.jpg');

/*Table structure for table `jobrequest` */

DROP TABLE IF EXISTS `jobrequest`;

CREATE TABLE `jobrequest` (
  `Jobrqst_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Agent_Id` int(11) NOT NULL,
  `Labour_Id` int(11) NOT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Jobrqst_date` date DEFAULT NULL,
  `cv` varchar(200) DEFAULT NULL,
  `Labour_Photo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Jobrqst_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `jobrequest` */

insert  into `jobrequest`(`Jobrqst_Id`,`Agent_Id`,`Labour_Id`,`Status`,`Jobrqst_date`,`cv`,`Labour_Photo`) values (1,2,4,'approved','2021-02-17','/static/mphoto/110321-122046.jpg','/static/mphoto/110321-122046.jpg'),(2,2,10,'approved','2021-03-11','/static/mphoto/110321-122046.jpg','/static/mphoto/110321-122046.jpg'),(3,2,10,'approved','2021-03-11','/static/mphoto/110321-122246.jpg','/static/mphoto/110321-122246.jpg'),(4,16,10,'pending','2021-05-05','/static/mphoto/050521-232953.jpg','/static/mphoto/050521-232953.jpg'),(5,16,10,'pending','2021-05-05','/static/mphoto/050521-233139.jpg','/static/mphoto/050521-233139.jpg'),(6,7,10,'pending','2021-05-05','/static/mphoto/050521-233525.jpg','/static/mphoto/050521-233525.jpg');

/*Table structure for table `laboursreg` */

DROP TABLE IF EXISTS `laboursreg`;

CREATE TABLE `laboursreg` (
  `Login_Id` int(11) NOT NULL,
  `Labour_name` varchar(20) DEFAULT NULL,
  `Labour_place` varchar(20) DEFAULT NULL,
  `Labour_post` varchar(20) DEFAULT NULL,
  `Labour_pin` int(11) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `State` varchar(20) DEFAULT NULL,
  `District` varchar(20) DEFAULT NULL,
  `Phone_no` bigint(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `Government_Id` varchar(20) DEFAULT NULL,
  `Id_no` int(11) DEFAULT NULL,
  `Id_image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Login_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `laboursreg` */

insert  into `laboursreg`(`Login_Id`,`Labour_name`,`Labour_place`,`Labour_post`,`Labour_pin`,`Age`,`DOB`,`Gender`,`State`,`District`,`Phone_no`,`Email`,`Government_Id`,`Id_no`,`Id_image`) values (4,'gujish','gatka','pochinki',26956,34,'2021-02-13','male','pubg','miltrybase',265952312,'vfgdfh','sfdgd',5352,'/static/mphoto/230321-120421.jpg'),(8,'somu','sdff','',0,0,'0000-00-00','radio','Karnataka','udupi',0,'','pan card',2147483647,'/static/mphoto/230321-120421.jpg'),(9,'seenu','hadpur','hadpur',12151,23,'0000-00-00','radio','Karnataka','udupi',2455656,'','aadar card',123654,'/static/mphoto/180421-101352.jpg'),(10,'seena','sdffdhggfd','gdfghdf',54,20,'0000-00-00','radio','Karnataka','kolapur',0,'seena@gmail.com','aadar card',0,'/static/mphoto/180421-101352.jpg'),(18,'ram','kpba','bpba',67056,25,'0000-00-00','radio','gujarat','porbandhar',678477,'ram@gmail.com','pan card',468644,'/static/mphoto/230321-120141.jpg'),(19,'rs','dg','gdsag',4324,45,'0000-00-00','radio','gujarat','porbandhar',435365475,'rs@gmail.com','aadar card',35453453,'/static/mphoto/230321-120421.jpg'),(21,'amal','kayal','kayal',567582,30,'1990-12-07','male','Nagaland','Silvassa',8689874565,'amal@gmail.com','Aadhaar Card',654897,'/static/mphoto/180421-101352.jpg');

/*Table structure for table `lfeedback` */

DROP TABLE IF EXISTS `lfeedback`;

CREATE TABLE `lfeedback` (
  `Feedback_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Labour_id` int(11) DEFAULT NULL,
  `Feedback` varchar(300) DEFAULT NULL,
  `Feedback_date` datetime DEFAULT NULL,
  PRIMARY KEY (`Feedback_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `lfeedback` */

insert  into `lfeedback`(`Feedback_Id`,`Labour_id`,`Feedback`,`Feedback_date`) values (1,4,'ghgusyyyytsiutiuutust','2021-02-03 12:13:35'),(2,10,'ygtujiuyjyhgtrf','2021-03-20 00:00:00'),(3,10,'yhhyugtf','2021-03-20 00:00:00'),(4,10,'brwkyefiyawdgtfiHSDGcilysd','2021-04-18 00:00:00'),(5,10,'brwkyefiyawdgtfiHSDGcilysd','2021-04-18 00:00:00'),(6,10,'brwkyefiyawdgtfiHSDGcilysd','2021-04-18 00:00:00'),(7,10,'brwkyefiyawdgtfiHSDGcilysd','2021-04-18 00:00:00'),(8,10,'adafsgds','2021-05-05 00:00:00');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_ID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Login_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_ID`,`username`,`password`,`Type`) values (1,'admin','3456','admin'),(2,'sudhakaran','1234','agent'),(4,'gujish','111','labour'),(5,'varun','123','customer'),(6,'lic','134','company'),(7,'susu@gmail.com','1234','agent'),(8,'somu','9876','labour'),(10,'seena@gmail.com','0258','labour'),(11,'aswin@gmail.com','0987','pending'),(12,'7asw','0987','customer'),(13,'aswinntholambra@gmail.com','5678','company'),(15,'ravi@gmail.com','2233','pending'),(16,'varun@gmail.com','varun','agent'),(17,'var@gmail.com','var','agent'),(18,'ram@gmail.com','ram','labour'),(19,'rs@gmail.com','rs','reject'),(20,'riyas@gmail.com','riyas123','agent'),(21,'amal@gmail.com','amal123','labour'),(22,'aswin@gmail.com','aswin123','customer'),(23,'js@gmail.com','js123','company'),(24,'shafi@gmail.com','shafi134','agent'),(25,'hdf1@gmail.com','hdf123','pending');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `Notification_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Notification` varchar(50) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  PRIMARY KEY (`Notification_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`Notification_Id`,`Notification`,`Date`) values (1,'treytjhdf','2021-02-07 00:00:00'),(2,'kkkkkkkk','2021-02-07 00:00:00'),(7,'ryydddddu57iiiiiiiiiiiiiiiiiihtddsa','2021-04-18 00:00:00'),(8,'asdf','2021-05-05 00:00:00'),(9,'hi','2021-05-06 00:00:00');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `Payment_Id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) NOT NULL,
  `Company_Id` int(11) NOT NULL,
  `Payment_amount` double DEFAULT NULL,
  `Payment_date` datetime DEFAULT NULL,
  PRIMARY KEY (`Payment_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`Payment_Id`,`request_id`,`Company_Id`,`Payment_amount`,`Payment_date`) values (1,2,0,34,'2021-03-21 12:50:05'),(2,2,0,1223,'2021-03-21 12:51:45');

/*Table structure for table `policy` */

DROP TABLE IF EXISTS `policy`;

CREATE TABLE `policy` (
  `policyid` int(11) NOT NULL AUTO_INCREMENT,
  `Company_Id` int(11) NOT NULL,
  `policy_name` varchar(100) DEFAULT NULL,
  `policy_details` varchar(50) DEFAULT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `duration` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`policyid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `policy` */

insert  into `policy`(`policyid`,`Company_Id`,`policy_name`,`policy_details`,`amount`,`duration`) values (1,6,'dghfjg',NULL,0,'1'),(2,13,'dfhggvcb cvcvx',NULL,2000,'1'),(3,13,'hjghfgghj',NULL,4000,'1'),(4,13,'',NULL,0,''),(5,13,'jeevan raksha',NULL,1000,'1'),(6,13,'jeevan aatma','high previliaged jeevan raksha ',1000,'1');

/*Table structure for table `policy_request` */

DROP TABLE IF EXISTS `policy_request`;

CREATE TABLE `policy_request` (
  `p_req_id` int(11) NOT NULL AUTO_INCREMENT,
  `Agent_Id` int(11) NOT NULL,
  `labourid` int(11) DEFAULT NULL,
  `policyid` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`p_req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `policy_request` */

insert  into `policy_request`(`p_req_id`,`Agent_Id`,`labourid`,`policyid`,`date`,`status`) values (2,2,4,'2','2021-03-21','approved'),(3,2,10,'2','2021-03-28','approved'),(4,2,10,'2','2021-04-18','approved'),(5,3,10,'2','2021-04-18','pending'),(6,2,4,'2','2021-05-06','pending');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `Request_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Customer_Id` int(11) NOT NULL,
  `Agent_Id` int(11) NOT NULL,
  `Work_Details` varchar(50) DEFAULT NULL,
  `Needed_labours` bigint(20) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Request_Date` datetime DEFAULT NULL,
  `work_days` int(11) DEFAULT NULL,
  `per_head` int(11) DEFAULT NULL,
  PRIMARY KEY (`Request_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`Request_Id`,`Customer_Id`,`Agent_Id`,`Work_Details`,`Needed_labours`,`Status`,`Request_Date`,`work_days`,`per_head`) values (1,5,2,'dtydgd',12,'approved','2021-02-01 13:57:01',NULL,NULL),(2,12,2,'nhgf',76,'approved','2021-03-20 15:05:56',3,452),(6,22,15,'thepp',12,'approved','2021-04-18 13:43:42',5,750),(7,22,7,'thepp',10,'approved','2021-05-05 23:36:42',23,600),(8,22,7,'thepp',4,'approved','2021-05-19 15:19:11',5,700);

/*Table structure for table `salary` */

DROP TABLE IF EXISTS `salary`;

CREATE TABLE `salary` (
  `Salary_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Agent_Id` int(11) NOT NULL,
  `Labours_Id` int(11) NOT NULL,
  `Salary_Amount` double DEFAULT NULL,
  `Salary_Date` datetime DEFAULT NULL,
  PRIMARY KEY (`Salary_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `salary` */

insert  into `salary`(`Salary_Id`,`Agent_Id`,`Labours_Id`,`Salary_Amount`,`Salary_Date`) values (1,2,4,656,'2021-03-07 00:00:00'),(2,2,10,5000,'2021-03-07 12:29:23'),(3,2,10,2300,'2021-05-05 23:20:59'),(4,2,8,20000,'2021-05-06 10:43:24'),(5,2,10,5000,'2021-05-11 18:33:31'),(6,2,4,45000,'2021-05-13 18:42:42');

/*Table structure for table `status` */

DROP TABLE IF EXISTS `status`;

CREATE TABLE `status` (
  `Status_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Agent_Id` int(11) NOT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  PRIMARY KEY (`Status_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `status` */

insert  into `status`(`Status_Id`,`Agent_Id`,`Status`,`Description`,`Date`) values (1,2,'5','fsd','2021-05-05 00:00:00'),(2,7,'10','wrery','2021-03-15 12:48:39'),(3,15,'5','thepp','2021-03-16 12:15:43'),(4,16,'3','tfhfgj','2021-03-16 12:16:10');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
