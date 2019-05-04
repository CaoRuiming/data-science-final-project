
SELECT 1, concat(0, substring(`Census Block FIPS Code`, 1, 4)) as County, avg(`Max Advertised Downstream Speed (mbps)`) as avgspeed
	FROM CA
    WHERE Consumer = 1 and (`Technology Code` = 40 or `Technology Code` = 41 or `Technology Code` = 42 or `Technology Code` = 43)
    -- WHERE Consumer = 1 and (`Technology Code` = 43 or `Technology Code` = 50)
    GROUP BY concat(0, substring(`Census Block FIPS Code`, 1, 4));