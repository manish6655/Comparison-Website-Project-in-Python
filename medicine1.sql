-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2021 at 07:14 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medicine1`
--

-- --------------------------------------------------------

--
-- Table structure for table `actual`
--

CREATE TABLE `actual` (
  `Sno` int(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Component` varchar(100) NOT NULL,
  `Company` varchar(100) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `actual`
--

INSERT INTO `actual` (`Sno`, `Name`, `Component`, `Company`, `Date`) VALUES
(1, 'paracetamol', 'Para Element ', 'DT para', '2020-12-23 18:30:00'),
(2, 'crocin', 'DT cr', 'DT Crosin', '2020-12-15 18:30:00'),
(3, 'calpol', 'dt cal', 'DT calpol', '0000-00-00 00:00:00'),
(7, 'crept', 'crep dd', 'crep cmp', '2020-12-19 18:50:12');

-- --------------------------------------------------------

--
-- Table structure for table `ecommerce`
--

CREATE TABLE `ecommerce` (
  `id` int(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `link` varchar(100) NOT NULL,
  `req` varchar(50) NOT NULL,
  `by_which` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ecommerce`
--

INSERT INTO `ecommerce` (`id`, `name`, `link`, `req`, `by_which`) VALUES
(1, 'Flipcart', 'https://www.flipkart.com/', 'q', 'name'),
(2, 'Amazon', 'https://www.amazon.com/', 'field-keywords', 'name'),
(3, 'Snapdeal', 'https://www.snapdeal.com/', 'keyword', 'name'),
(4, 'Myntra', 'https://www.myntra.com/', '//input[@class=\"desktop-searchBar\"]', 'xpath'),
(5, 'Alibaba', 'https://www.alibaba.com/', 'SearchText', 'name');

-- --------------------------------------------------------

--
-- Table structure for table `generic`
--

CREATE TABLE `generic` (
  `Sno` int(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Component` varchar(100) NOT NULL,
  `Company` varchar(100) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `generic`
--

INSERT INTO `generic` (`Sno`, `Name`, `Component`, `Company`, `Date`) VALUES
(8, 'crocin-dt2', 'crocin-cnj', 'crocin-cmpny', '2020-12-20 14:13:10'),
(11, 'crocin-ab1', 'crocin-ab1', 'crocin-ab1', '2020-12-30 04:57:06'),
(12, 'crocin-ab2', 'crocin-ab2', 'crocin-ab2', '2020-12-30 04:57:06'),
(13, 'crocin-dt4', 'crocin-dt4', 'crocin-dt4', '2020-12-30 05:06:12'),
(31, 'paracetamol-abc dt2', 'cmp dt2', 'company-dt2', '2021-01-04 17:21:35'),
(32, 'paracetamol-abc dt3', 'cmp dt3', 'company-dt3', '2021-01-04 17:21:35'),
(33, 'paracetamol-abc dt4', 'cmp dt4', 'company-dt4', '2021-01-04 17:21:35'),
(34, 'paracetamol-abc dt5', 'cmp dt5', 'company-dt5', '2021-01-04 17:21:35'),
(35, 'paracetamol-abc dt6', 'cmp dt6', 'company-dt6', '2021-01-04 17:21:35'),
(36, 'paracetamol-abc dt7', 'cmp dt7', 'company-dt7', '2021-01-04 17:21:35'),
(39, 'crocin-abc dt1', 'cmp dt1', 'company-dt1', '2021-01-04 17:22:53'),
(40, 'crocin-abc dt2', 'cmp dt2', 'company-dt2', '2021-01-04 17:22:53'),
(41, 'crocin-abc dt3', 'cmp dt3', 'company-dt3', '2021-01-04 17:22:53'),
(42, 'crocin-abc dt4', 'cmp dt4', 'company-dt4', '2021-01-04 17:22:53'),
(43, 'crocin-abc dt5', 'cmp dt5', 'company-dt5', '2021-01-04 17:22:53'),
(44, 'crocin-abc dt6', 'cmp dt6', 'company-dt6', '2021-01-04 17:22:53'),
(45, 'crocin-abc dt7', 'cmp dt7', 'company-dt7', '2021-01-04 17:22:53'),
(46, 'crocin-abc dt8', 'cmp dt8', 'company-dt8', '2021-01-04 17:22:53'),
(47, 'crocin-abc dt9', 'cmp dt9', 'company-dt9', '2021-01-04 17:22:53'),
(48, 'crept-abc dt1', 'cmp dt1', 'company-dt1', '2021-01-04 18:56:53'),
(49, 'crept-abc dt2', 'cmp dt2', 'company-dt2', '2021-01-04 18:56:53'),
(50, 'crept-abc dt3', 'cmp dt3', 'company-dt3', '2021-01-04 18:56:53'),
(51, 'crept-abc dt4', 'cmp dt4', 'company-dt4', '2021-01-04 18:56:53'),
(52, 'crept-abc dt5', 'cmp dt5', 'company-dt5', '2021-01-04 18:56:53'),
(53, 'crept-abc dt6', 'cmp dt6', 'company-dt6', '2021-01-04 18:56:53'),
(54, 'crept-abc dt7', 'cmp dt7', 'company-dt7', '2021-01-04 18:56:53'),
(55, 'crept-abc dt8', 'cmp dt8', 'company-dt8', '2021-01-04 18:56:53'),
(56, 'crept-abc dt9', 'cmp dt9', 'company-dt9', '2021-01-04 18:56:53'),
(57, 'paracetamol-abc dt st', 'cmp dt1', 'company-dt1', '2021-01-06 18:26:32'),
(58, 'paracetamol-abc dt st', 'cmp dt2', 'company-dt2', '2021-01-06 18:26:32');

-- --------------------------------------------------------

--
-- Table structure for table `itemsearch`
--

CREATE TABLE `itemsearch` (
  `id` int(50) NOT NULL,
  `itemname` varchar(50) NOT NULL,
  `path` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `itemsearch`
--

INSERT INTO `itemsearch` (`id`, `itemname`, `path`) VALUES
(1, 'medicine', '/medicine'),
(2, 'ecommerce', '/e_commerce'),
(3, 'medicine dashboard', '/md_dashboard'),
(4, 'help', '/help'),
(5, 'about', '/about'),
(6, 'feedback', '/feedback');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Id` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Username`, `Password`, `Id`) VALUES
('deepak', 'deepak@123', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actual`
--
ALTER TABLE `actual`
  ADD PRIMARY KEY (`Sno`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- Indexes for table `ecommerce`
--
ALTER TABLE `ecommerce`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `generic`
--
ALTER TABLE `generic`
  ADD PRIMARY KEY (`Sno`);

--
-- Indexes for table `itemsearch`
--
ALTER TABLE `itemsearch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actual`
--
ALTER TABLE `actual`
  MODIFY `Sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `ecommerce`
--
ALTER TABLE `ecommerce`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `generic`
--
ALTER TABLE `generic`
  MODIFY `Sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `itemsearch`
--
ALTER TABLE `itemsearch`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `Id` int(40) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
