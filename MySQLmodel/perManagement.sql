-- MySQL Script generated by MySQL Workbench
-- Fri Oct 11 10:18:35 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema PerManagement
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema PerManagement
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `PerManagement` DEFAULT CHARACTER SET utf8 ;
USE `PerManagement` ;

-- -----------------------------------------------------
-- Table `PerManagement`.`Department`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PerManagement`.`Department` (
  `idDepartment` CHAR(3) NOT NULL,
  `DepartmentName` VARCHAR(45) NULL,
  `DepartmentComment` VARCHAR(45) NULL,
  PRIMARY KEY (`idDepartment`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PerManagement`.`Team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PerManagement`.`Team` (
  `idTeam` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idTeam`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PerManagement`.`Title`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PerManagement`.`Title` (
  `idTitle` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idTitle`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PerManagement`.`WorkPosition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PerManagement`.`WorkPosition` (
  `idWorkPosition` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idWorkPosition`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PerManagement`.`Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PerManagement`.`Person` (
  `idPerson` CHAR(8) NOT NULL,
  `PersonPho` MEDIUMTEXT NULL,
  `PersonName` VARCHAR(30) NULL,
  `PersonBirthDate` DATE NULL,
  `PersonNation` VARCHAR(5) NULL,
  `PersonPoliticalOutlook` VARCHAR(6) NULL,
  `PersonIsMarry` TINYINT NULL,
  `PersonidTitle` INT NULL,
  `PersoncolMajor` VARCHAR(10) NULL,
  `PersonEducation` ENUM('本科', '专科', '硕士', '博士') NULL,
  `PersonGraduationSchool` VARCHAR(10) NULL,
  `PersonGraduationDate` DATE NULL,
  `PersonBaseSalary` DECIMAL NULL,
  `PersonIDNumber` VARCHAR(18) NULL,
  `PersonDepartementNum` VARCHAR(3) NULL,
  `PersonWorkPosition` INT NULL,
  `PersonidTeam` INT NULL,
  `PersonAdmissionDate` DATE NULL,
  `PersonParticipateDate` DATE NULL,
  `PersonCategory` ENUM('工人', '干部', '临时工') NULL,
  `PersoncolContractPeriod` INT NULL,
  `PersonFamilyAddress` VARCHAR(45) NULL,
  `PersonContactInformation` VARCHAR(11) NULL,
  `PersonComment` VARCHAR(45) NULL,
  `PersonGender` ENUM('男', '女') NULL,
  `PersonState` ENUM('在职', '离退') NULL,
  PRIMARY KEY (`idPerson`),
  INDEX `departmentNumber_idx` (`PersonDepartementNum` ASC),
  INDEX `personTeam_idx` (`PersonidTeam` ASC),
  INDEX `personTitle_idx` (`PersonidTitle` ASC),
  INDEX `personWorkPosition_idx` (`PersonWorkPosition` ASC),
  CONSTRAINT `departmentNumber`
    FOREIGN KEY (`PersonDepartementNum`)
    REFERENCES `PerManagement`.`Department` (`idDepartment`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `personTeam`
    FOREIGN KEY (`PersonidTeam`)
    REFERENCES `PerManagement`.`Team` (`idTeam`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `personTitle`
    FOREIGN KEY (`PersonidTitle`)
    REFERENCES `PerManagement`.`Title` (`idTitle`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `personWorkPosition`
    FOREIGN KEY (`PersonWorkPosition`)
    REFERENCES `PerManagement`.`WorkPosition` (`idWorkPosition`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PerManagement`.`Salary`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PerManagement`.`Salary` (
  `idSalary` INT NOT NULL AUTO_INCREMENT,
  `SalaryCardNumber` VARCHAR(20) NULL,
  `SalaryidPerson` CHAR(8) NULL,
  `SalaryBase` DECIMAL NULL,
  `SalaryWorkYears` INT NULL,
  `SalaryWorkYearsAllowance` DECIMAL NULL,
  `SalaryFoodSubsidy` DECIMAL NULL,
  `SalaryMan-hourCompletionRate` VARCHAR(5) NULL DEFAULT '0%',
  `SalaryQualityVetoCoefficient` VARCHAR(5) NULL DEFAULT '0%',
  `SalaryAttendanceDays` INT NULL DEFAULT 0,
  `SalaryBasicPay` DECIMAL NULL,
  `SalarycolWorkSubsidy` DECIMAL NULL,
  `SalaryHouseSubsidy` DECIMAL NULL,
  `SalaryHealthFee` DECIMAL NULL,
  `SalaryNightSnackFee` DECIMAL NULL,
  `SalaryOvertimeFee` DECIMAL NULL,
  `SalaryMaternityLeave` INT NULL,
  `SalaryFlexibleSubsidy` DECIMAL NULL,
  `SalaryFlexibleDeduction` DECIMAL NULL,
  `SalaryTeamSubsidy` DECIMAL NULL,
  `SalaryPayable` DECIMAL NULL,
  `SalaryInsuranceMoney` DECIMAL NULL,
  `SalaryPayFund` DECIMAL NULL,
  `SalaryIncomeTax` DECIMAL NULL,
  `SalaryDeduction` DECIMAL NULL,
  `SalaryHouseFee` DECIMAL NULL,
  `SalarWaterFee` DECIMAL NULL,
  `SalaryElectricityFee` DECIMAL NULL,
  `SalaryReal` DECIMAL NULL,
  `SalaryComment` VARCHAR(45) NULL,
  `SalaryidDepartment` CHAR(3) NULL,
  `SalaryidTeam` INT NULL,
  `SalaryidTitle` INT NULL,
  `SalaryidWorkPosition` INT NULL,
  `SalaryPayDate` DATE NULL,
  PRIMARY KEY (`idSalary`),
  INDEX `idPerson_idx` (`SalaryidPerson` ASC),
  INDEX `salaryDepartment_idx` (`SalaryidDepartment` ASC),
  INDEX `salaryTeam_idx` (`SalaryidTeam` ASC),
  INDEX `salaryTitle_idx` (`SalaryidTitle` ASC),
  INDEX `salaryWorkPosition_idx` (`SalaryidWorkPosition` ASC),
  CONSTRAINT `idPerson`
    FOREIGN KEY (`SalaryidPerson`)
    REFERENCES `PerManagement`.`Person` (`idPerson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `salaryDepartment`
    FOREIGN KEY (`SalaryidDepartment`)
    REFERENCES `PerManagement`.`Department` (`idDepartment`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `salaryTeam`
    FOREIGN KEY (`SalaryidTeam`)
    REFERENCES `PerManagement`.`Team` (`idTeam`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `salaryTitle`
    FOREIGN KEY (`SalaryidTitle`)
    REFERENCES `PerManagement`.`Title` (`idTitle`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `salaryWorkPosition`
    FOREIGN KEY (`SalaryidWorkPosition`)
    REFERENCES `PerManagement`.`WorkPosition` (`idWorkPosition`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PerManagement`.`PublicFund`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PerManagement`.`PublicFund` (
  `idPublicFund` INT NOT NULL AUTO_INCREMENT,
  `PublicFundAccount` VARCHAR(45) NULL,
  `PublicFundidPerson` CHAR(8) NULL,
  PRIMARY KEY (`idPublicFund`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
