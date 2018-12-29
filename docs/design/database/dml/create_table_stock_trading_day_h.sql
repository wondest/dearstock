DROP TABLE IF EXISTS `dearstock`.`stock_trading_day_h`;

CREATE TABLE `dearstock`.`stock_trading_day_h` (
  `date` DATE NOT NULL,
  `change` DECIMAL(7,5) NULL,
  `open` DECIMAL(10,2) NULL,
  `preclose` DECIMAL(10,2) NULL,
  `close` DECIMAL(10,2) NULL,
  `high` DECIMAL(10,2) NULL,
  `low` DECIMAL(10,2) NULL,
  `volume` BIGINT NULL,
  `amount` DECIMAL(16,2) NULL,
  `code` VARCHAR(6) NULL,
  `symbol` VARCHAR(8) NOT NULL,
  `modify_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`date`, `symbol`))
COMMENT = '股票日交易历史表';