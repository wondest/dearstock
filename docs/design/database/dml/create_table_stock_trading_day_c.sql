DROP TABLE IF EXISTS `dearstock`.`stock_trading_day_c`;

CREATE TABLE `dearstock`.`stock_trading_day_c` (
  `date` DATE NOT NULL,
  `code` VARCHAR(6) NULL,
  `symbol` VARCHAR(8) NOT NULL,
  `name` VARCHAR(45) NULL,
  `change` DECIMAL(7,5) NULL,
  `trade` DECIMAL(10,2) NULL,
  `open` DECIMAL(10,2) NULL,
  `high` DECIMAL(10,2) NULL,
  `low` DECIMAL(10,2) NULL,
  `close` DECIMAL(10,2) NULL,
  `volume` BIGINT(20) NULL,
  `turnoverratio` DECIMAL(7,5) NULL,
  `amount` DECIMAL(16,2) NULL,
  `per` DECIMAL(10,5) NULL,
  `pb` DECIMAL(10,5) NULL,
  `mktcap` DECIMAL(20,2) NULL,
  `nmc` DECIMAL(18,2) NULL,
  `modify_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`date`, `symbol`))
COMMENT = '股票交易快照表';