# format data into an excel
# Tyler Piazza

keys = ['AAPL percent', 'boston humidity', 'microsoft trend', 'MSFT price', 'MSFT volume', 'AMZN price', 'apple trend', 'AMZN percent', 'AAPL volume', 'new york city humidity', 'facebook trend', 'AAPL price', 'boston temperature', 'AMZN volume', 'amazon trend', 'FB volume', 'los angeles temperature', 'FB percent', 'new york city temperature', 'los angeles humidity', 'MSFT percent', 'FB price', 'minutes']

remember_rows.append(keys)
remember_rows.append([0.020439, 81.0, 5.0, 111.7, 13722486.0, 1767.92, 15.0, 0.046001, 17268729.0, 65.0, 50.0, 182.23, 55.0, 3482297.0, 45.0, 9420592.0, 54.0, 0.017424, 54.0, 54.0, 0.007305000000000001, 143.06, 675])


remember_rows.append([0.020832000000000003, 81.0, 5.0, 111.62, 13799500.0, 1767.99, 15.0, 0.046043, 17370636.0, 65.0, 50.0, 182.3001, 55.0, 3500778.0, 45.0, 9504874.0, 54.0, 0.016996999999999998, 54.0, 54.0, 0.006583, 143.0, 677])

remember_rows.append( [0.021391, 81.0, 5.0, 111.6792, 13888353.0, 1769.004, 15.0, 0.046643, 17453382.0, 65.0, 49.0, 182.4, 55.0, 3509624.0, 45.0, 9553283.0, 54.0, 0.017424, 54.0, 54.0, 0.007117, 143.06, 678])
remember_rows.append( [0.021446999999999997, 81.0, 5.0, 111.83, 14074779.0, 1768.51, 15.0, 0.046349999999999995, 17616344.0, 65.0, 49.0, 182.41, 55.0, 3538069.0, 45.0, 9648896.0, 54.0, 0.017637, 54.0, 54.0, 0.008477, 143.09, 679])
remember_rows.append( [0.021223000000000002, 81.0, 5.0, 111.78, 14158665.0, 1768.89, 15.0, 0.046575, 17680237.0, 65.0, 50.0, 182.37, 55.0, 3545152.0, 47.0, 9685850.0, 54.0, 0.017922, 54.0, 54.0, 0.008026, 143.13, 680])
remember_rows.append( [0.021055, 81.0, 5.0, 111.77, 14205693.0, 1768.07, 15.0, 0.04609, 17744544.0, 65.0, 50.0, 182.34, 55.0, 3554976.0, 47.0, 9729339.0, 54.0, 0.017922, 54.0, 54.0, 0.007936, 143.13, 681])
remember_rows.append( [0.021783, 81.0, 5.0, 111.795, 14254785.0, 1770.95, 15.0, 0.047793999999999996, 17794128.0, 65.0, 48.0, 182.47, 55.0, 3572961.0, 45.0, 9798972.0, 54.0, 0.019842, 54.0, 54.0, 0.008161, 143.4, 682])
remember_rows.append( [0.022007, 81.0, 5.0, 111.78, 14327644.0, 1769.75, 15.0, 0.047084, 17874256.0, 65.0, 48.0, 182.51, 55.0, 3592110.0, 45.0, 9874289.0, 54.0, 0.019344, 54.0, 54.0, 0.008026, 143.33, 683])
remember_rows.append( [0.021894999999999998, 81.0, 6.0, 111.6268, 14405674.0, 1768.0, 15.0, 0.046049, 17967944.0, 65.0, 49.0, 182.49, 55.0, 3602415.0, 44.0, 9936306.0, 54.0, 0.018876999999999998, 54.0, 54.0, 0.006644, 143.2643, 684])
remember_rows.append( [0.021727, 81.0, 6.0, 111.8, 14488896.0, 1770.7, 15.0, 0.047645999999999994, 18020131.0, 65.0, 49.0, 182.46, 55.0, 3618529.0, 44.0, 9991288.0, 54.0, 0.019598, 54.0, 54.0, 0.008206, 143.3657, 685])
remember_rows.append( [0.019935, 81.0, 6.0, 111.77, 14619715.0, 1768.0, 15.0, 0.046049, 18129693.0, 65.0, 49.0, 182.14, 55.0, 3636628.0, 47.0, 10055540.0, 54.0, 0.018277, 54.0, 54.0, 0.007936, 143.18, 686])
remember_rows.append( [0.019711, 81.0, 6.0, 111.69, 14714434.0, 1767.3192, 15.0, 0.045646000000000006, 18209269.0, 65.0, 49.0, 182.1, 55.0, 3650132.0, 47.0, 10113482.0, 54.0, 0.018171, 54.0, 54.0, 0.007214000000000001, 143.165, 687])

remember_rows.append( [0.019207000000000002, 81.0, 5.0, 111.6801, 14836800.0, 1767.6044, 15.0, 0.045815, 18320849.0, 65.0, 50.0, 182.01, 55.0, 3662313.0, 44.0, 10202479.0, 54.0, 0.017851, 54.0, 54.0, 0.007125, 143.12, 689])
remember_rows.append( [0.020545, 81.0, 5.0, 111.875, 14882951.0, 1770.3, 15.0, 0.047409, 18371458.0, 65.0, 50.0, 182.249, 55.0, 3674144.0, 44.0, 10287441.0, 54.0, 0.018775, 54.0, 54.0, 0.008883, 143.25, 690])
remember_rows.append( [0.021111, 81.0, 5.0, 111.895, 14954716.0, 1770.1, 15.0, 0.047291, 18424461.0, 65.0, 49.0, 182.35, 55.0, 3684279.0, 45.0, 10333131.0, 54.0, 0.018918, 54.0, 54.0, 0.009063, 143.27, 691])
remember_rows.append( [0.021055, 81.0, 5.0, 111.911, 15007985.0, 1771.2511, 15.0, 0.047972, 18476391.0, 65.0, 49.0, 182.34, 55.0, 3704726.0, 45.0, 10358178.0, 54.0, 0.019771, 54.0, 54.0, 0.009207, 143.39, 692])
remember_rows.append( [0.021398999999999998, 81.0, 6.0, 112.035, 15142267.0, 1771.54, 15.0, 0.048143000000000005, 18559707.0, 65.0, 50.0, 182.4014, 55.0, 3721308.0, 46.0, 10447213.0, 55.0, 0.019415, 54.0, 50.0, 0.010326, 143.34, 693])
remember_rows.append( [0.021167, 81.0, 6.0, 111.91, 15198952.0, 1771.3082, 15.0, 0.048006, 18592496.0, 58.0, 50.0, 182.36, 55.0, 3732782.0, 46.0, 10488495.0, 55.0, 0.020307, 54.0, 50.0, 0.009198, 143.4653, 694])
remember_rows.append( [0.021055, 71.0, 5.0, 111.9, 15255016.0, 1772.47, 15.0, 0.048693, 18645601.0, 58.0, 50.0, 182.34, 57.0, 3741600.0, 46.0, 10550516.0, 55.0, 0.021331000000000003, 54.0, 50.0, 0.009108, 143.6094, 695])
remember_rows.append( [0.020775000000000002, 71.0, 5.0, 111.91, 15358202.0, 1771.88, 15.0, 0.048344, 18700772.0, 58.0, 50.0, 182.29, 57.0, 3752938.0, 46.0, 10602810.0, 55.0, 0.020915, 54.0, 50.0, 0.009198, 143.5509, 696])
remember_rows.append( [0.021167, 71.0, 6.0, 111.94, 15389216.0, 1773.0, 15.0, 0.049006999999999995, 18733920.0, 58.0, 50.0, 182.36, 57.0, 3772469.0, 45.0, 10630897.0, 55.0, 0.021122000000000002, 54.0, 50.0, 0.009469, 143.58, 697])
remember_rows.append( [0.020775000000000002, 71.0, 6.0, 111.895, 15457435.0, 1771.43, 15.0, 0.048078, 18778597.0, 58.0, 50.0, 182.29, 57.0, 3782980.0, 45.0, 10660008.0, 55.0, 0.020269, 54.0, 50.0, 0.009063, 143.46, 698])

remember_rows.append( [0.021335000000000003, 71.0, 5.0, 111.87, 15503593.0, 1771.17, 14.0, 0.047923999999999994, 18825962.0, 58.0, 48.0, 182.39, 57.0, 3795696.0, 43.0, 10702842.0, 55.0, 0.019629, 54.0, 50.0, 0.008838, 143.37, 700])
remember_rows.append( [0.021341000000000002, 71.0, 5.0, 111.88, 15537118.0, 1770.3324, 14.0, 0.047429, 18883133.0, 58.0, 48.0, 182.391, 57.0, 3807193.0, 43.0, 10743747.0, 55.0, 0.019273, 54.0, 50.0, 0.008928, 143.32, 701])
remember_rows.append( [0.019863, 71.0, 5.0, 111.735, 15596998.0, 1768.46, 15.0, 0.046321, 18963616.0, 58.0, 50.0, 182.1271, 57.0, 3826424.0, 45.0, 10805895.0, 55.0, 0.017993, 54.0, 50.0, 0.00762, 143.14, 702])
remember_rows.append( [0.019095, 71.0, 5.0, 111.68, 15708729.0, 1767.57, 15.0, 0.045793999999999994, 19062844.0, 58.0, 50.0, 181.99, 57.0, 3847041.0, 45.0, 10858049.0, 55.0, 0.017566, 54.0, 50.0, 0.007124, 143.08, 703])
remember_rows.append( [0.018423000000000002, 71.0, 6.0, 111.59, 15746743.0, 1766.9333, 15.0, 0.045418, 19126689.0, 58.0, 50.0, 181.87, 57.0, 3860590.0, 44.0, 10909690.0, 55.0, 0.017495, 54.0, 50.0, 0.006313, 143.07, 704])
remember_rows.append( [0.018031, 71.0, 6.0, 111.49, 15829424.0, 1764.9751, 15.0, 0.04425900000000001, 19262416.0, 58.0, 50.0, 181.8, 57.0, 3872309.0, 44.0, 10987761.0, 55.0, 0.016073, 54.0, 50.0, 0.005411, 142.87, 705])
remember_rows.append([0.018408, 71.0, 5.0, 111.53, 15879320.0, 1766.43, 14.0, 0.04511999999999999, 19308949.0, 58.0, 47.0, 181.8673, 57.0, 3885070.0, 42.0, 11041052.0, 55.0, 0.017993, 54.0, 50.0, 0.005770999999999999, 143.14, 706])
remember_rows.append( [0.018143, 71.0, 5.0, 111.54, 15915901.0, 1766.9489, 14.0, 0.045427, 19356449.0, 58.0, 47.0, 181.82, 57.0, 3898332.0, 42.0, 11077296.0, 55.0, 0.018562000000000002, 54.0, 50.0, 0.005862000000000001, 143.22, 707])
remember_rows.append( [0.018031, 71.0, 5.0, 111.51, 15957249.0, 1767.0, 14.0, 0.045457, 19403607.0, 58.0, 47.0, 181.8, 57.0, 3904776.0, 42.0, 11119683.0, 55.0, 0.018846, 54.0, 50.0, 0.0055910000000000005, 143.26, 708])
remember_rows.append( [0.018062, 71.0, 5.0, 111.7, 16004213.0, 1768.19, 14.0, 0.046161, 19575820.0, 58.0, 47.0, 181.8056, 57.0, 3914176.0, 42.0, 11153456.0, 55.0, 0.020055, 54.0, 50.0, 0.007305000000000001, 143.43, 709])

remember_rows.append( [0.018451, 71.0, 5.0, 111.7, 16026441.0, 1769.41, 14.0, 0.046883, 19718875.0, 58.0, 48.0, 181.875, 57.0, 3930387.0, 43.0, 11192396.0, 55.0, 0.020553, 54.0, 50.0, 0.007305000000000001, 143.5, 710])
remember_rows.append( [0.018199, 71.0, 5.0, 111.66, 16101528.0, 1769.99, 14.0, 0.047226, 19800783.0, 58.0, 48.0, 181.83, 57.0, 3943735.0, 43.0, 11236858.0, 55.0, 0.020339999999999997, 54.0, 50.0, 0.0069440000000000005, 143.47, 711])
remember_rows.append( [0.017807, 71.0, 5.0, 111.58, 16144247.0, 1769.0948, 14.0, 0.046696, 19907774.0, 58.0, 48.0, 181.76, 57.0, 3949552.0, 44.0, 11283542.0, 55.0, 0.020339999999999997, 54.0, 50.0, 0.006222, 143.47, 712])
remember_rows.append( [0.017608, 71.0, 5.0, 111.53, 16195158.0, 1768.48, 14.0, 0.046333, 19960318.0, 58.0, 48.0, 181.7245, 57.0, 3956144.0, 44.0, 11325779.0, 55.0, 0.020696, 54.0, 50.0, 0.005770999999999999, 143.52, 714])
remember_rows.append( [0.016967, 71.0, 5.0, 111.51, 16253638.0, 1766.66, 15.0, 0.045256, 20027476.0, 58.0, 48.0, 181.61, 57.0, 3961925.0, 43.0, 11370610.0, 55.0, 0.020411000000000002, 54.0, 50.0, 0.0055910000000000005, 143.48, 715])
remember_rows.append( [0.017191, 71.0, 5.0, 111.49, 16308275.0, 1766.0458, 15.0, 0.044892, 20108725.0, 58.0, 48.0, 181.65, 57.0, 3975067.0, 43.0, 11408347.0, 55.0, 0.019771, 54.0, 50.0, 0.005411, 143.39, 716])
remember_rows.append( [0.014866999999999998, 71.0, 5.0, 111.39, 16352206.0, 1764.065, 14.0, 0.04372, 20233986.0, 58.0, 46.0, 181.235, 57.0, 3985858.0, 43.0, 11443421.0, 55.0, 0.018918, 54.0, 50.0, 0.004509, 143.27, 717])
remember_rows.append( [0.016407, 71.0, 5.0, 111.47, 16389492.0, 1763.82, 14.0, 0.043575, 20324226.0, 58.0, 46.0, 181.51, 57.0, 3998211.0, 43.0, 11463677.0, 55.0, 0.019344, 54.0, 50.0, 0.00523, 143.33, 718])
remember_rows.append( [0.015231, 71.0, 5.0, 111.235, 16499492.0, 1759.3048, 14.0, 0.040903999999999996, 20415254.0, 58.0, 47.0, 181.3, 57.0, 4040271.0, 42.0, 11511312.0, 55.0, 0.017531, 54.0, 50.0, 0.003111, 143.075, 719])
remember_rows.append( [0.016239, 71.0, 5.0, 111.46, 16554942.0, 1757.0, 14.0, 0.03954, 20484292.0, 58.0, 47.0, 181.48, 57.0, 4074301.0, 42.0, 11545637.0, 55.0, 0.018562000000000002, 54.0, 50.0, 0.0051400000000000005, 143.22, 720])

remember_rows.append(  [0.018927, 71.0, 5.0, 111.65, 17457547.0, 1763.48, 15.0, 0.043373999999999996, 21721836.0, 58.0, 49.0, 181.96, 57.0, 4316836.0, 45.0, 12294601.0, 55.0, 0.019344, 54.0, 50.0, 0.006854, 143.33, 746])
remember_rows.append( [0.019039, 71.0, 5.0, 111.65, 17490095.0, 1763.49, 15.0, 0.04338, 21762001.0, 58.0, 49.0, 181.98, 57.0, 4321805.0, 45.0, 12314122.0, 55.0, 0.018989, 54.0, 50.0, 0.006854, 143.28, 747])
remember_rows.append( [0.018815, 71.0, 5.0, 111.63, 17519976.0, 1762.7339, 15.0, 0.042933000000000006, 21791640.0, 58.0, 49.0, 181.94, 57.0, 4327214.0, 45.0, 12339421.0, 55.0, 0.018491, 54.0, 50.0, 0.006673, 143.21, 748])
remember_rows.append( [0.018367, 71.0, 5.0, 111.63, 17536120.0, 1763.4034, 15.0, 0.043329000000000006, 21824737.0, 58.0, 49.0, 181.86, 57.0, 4332214.0, 45.0, 12362844.0, 55.0, 0.018796, 54.0, 50.0, 0.006673, 143.2529, 749])
remember_rows.append( [0.019319, 71.0, 5.0, 111.7173, 17581559.0, 1765.08, 15.0, 0.044321, 21878170.0, 58.0, 49.0, 182.03, 57.0, 4342602.0, 45.0, 12389061.0, 55.0, 0.019927, 54.0, 50.0, 0.007461, 143.4119, 750])
remember_rows.append( [0.020103, 71.0, 5.0, 111.8399, 17638196.0, 1765.3774, 15.0, 0.044497, 21923899.0, 58.0, 49.0, 182.17, 57.0, 4352369.0, 45.0, 12429418.0, 55.0, 0.020553, 54.0, 50.0, 0.008566, 143.5, 751])
remember_rows.append( [0.020158999999999996, 71.0, 5.0, 111.845, 17682455.0, 1767.07, 15.0, 0.045498000000000004, 21971727.0, 58.0, 50.0, 182.18, 57.0, 4363491.0, 45.0, 12492197.0, 58.0, 0.020339999999999997, 54.0, 42.0, 0.008612, 143.47, 752])
remember_rows.append( [0.019879, 71.0, 5.0, 111.82, 17712465.0, 1766.65, 15.0, 0.045250000000000005, 22002114.0, 58.0, 50.0, 182.13, 57.0, 4372664.0, 45.0, 12515992.0, 58.0, 0.020347, 54.0, 42.0, 0.008387, 143.471, 753])
remember_rows.append( [0.020411000000000002, 71.0, 5.0, 111.9331, 17741917.0, 1767.6519, 16.0, 0.045842999999999995, 22042347.0, 57.0, 49.0, 182.225, 57.0, 4381379.0, 45.0, 12563636.0, 58.0, 0.02162, 53.0, 42.0, 0.009407, 143.65, 754])
remember_rows.append( [0.020551, 57.0, 5.0, 111.92, 17780512.0, 1768.5, 16.0, 0.046344, 22086014.0, 57.0, 49.0, 182.25, 56.0, 4400495.0, 45.0, 12601593.0, 58.0, 0.02098, 53.0, 42.0, 0.009288, 143.56, 756])

remember_rows.append( [0.020215, 57.0, 5.0, 111.88, 17815433.0, 1766.805, 16.0, 0.045342, 22138753.0, 57.0, 50.0, 182.19, 56.0, 4411441.0, 44.0, 12634356.0, 58.0, 0.020623999999999997, 53.0, 42.0, 0.008928, 143.51, 757])
remember_rows.append( [0.020327, 57.0, 5.0, 111.88, 17842673.0, 1766.24, 16.0, 0.045007, 22190018.0, 57.0, 50.0, 182.21, 56.0, 4417146.0, 44.0, 12653832.0, 58.0, 0.020198, 53.0, 42.0, 0.008928, 143.45, 758])
remember_rows.append( [0.020327, 57.0, 5.0, 111.89, 17860832.0, 1765.82, 16.0, 0.044759, 22246242.0, 57.0, 50.0, 182.21, 56.0, 4423661.0, 45.0, 12693477.0, 58.0, 0.0197, 53.0, 42.0, 0.009018, 143.38, 759])
remember_rows.append( [0.020327, 57.0, 5.0, 111.87, 17892233.0, 1765.1176, 16.0, 0.044343, 22299370.0, 57.0, 50.0, 182.21, 56.0, 4428444.0, 45.0, 12716025.0, 58.0, 0.018989, 53.0, 42.0, 0.008838, 143.28, 760])
remember_rows.append( [0.020103, 57.0, 5.0, 111.86, 17912226.0, 1766.19, 15.0, 0.044978, 22325890.0, 57.0, 49.0, 182.17, 56.0, 4434879.0, 43.0, 12729057.0, 58.0, 0.018349, 53.0, 42.0, 0.008747, 143.19, 761])
remember_rows.append( [0.019542999999999998, 57.0, 5.0, 111.8, 17942496.0, 1764.8835, 15.0, 0.044204999999999994, 22356108.0, 57.0, 49.0, 182.07, 56.0, 4443062.0, 43.0, 12751003.0, 58.0, 0.018277, 53.0, 42.0, 0.008206, 143.18, 762])
remember_rows.append( [0.019711, 57.0, 5.0, 111.8047, 17965736.0, 1764.61, 15.0, 0.044043, 22380739.0, 57.0, 49.0, 182.1, 56.0, 4449732.0, 45.0, 12762428.0, 58.0, 0.018547, 53.0, 42.0, 0.008249, 143.2179, 763])
remember_rows.append( [0.019207000000000002, 57.0, 5.0, 111.7128, 18007842.0, 1763.56, 15.0, 0.043422, 22422342.0, 57.0, 49.0, 182.01, 56.0, 4457507.0, 45.0, 12777145.0, 58.0, 0.018420000000000002, 53.0, 42.0, 0.0074199999999999995, 143.2, 764])
remember_rows.append( [0.019251, 57.0, 5.0, 111.707, 18040236.0, 1763.8033, 15.0, 0.043566, 22445846.0, 57.0, 50.0, 182.0179, 56.0, 4461657.0, 46.0, 12801601.0, 58.0, 0.019197, 53.0, 42.0, 0.007368, 143.3093, 765])
remember_rows.append( [0.019375, 57.0, 5.0, 111.679, 18072659.0, 1763.9799, 15.0, 0.04367, 22474487.0, 57.0, 50.0, 182.04, 56.0, 4468248.0, 46.0, 12819588.0, 58.0, 0.0197, 53.0, 42.0, 0.007115, 143.38, 766])

remember_rows.append( [0.019678, 57.0, 5.0, 111.66, 18122059.0, 1764.15, 15.0, 0.043771000000000004, 22501042.0, 57.0, 50.0, 182.0941, 56.0, 4474822.0, 46.0, 12840968.0, 58.0, 0.019902, 53.0, 42.0, 0.0069440000000000005, 143.4084, 767])
remember_rows.append( [0.019711, 57.0, 5.0, 111.68, 18200067.0, 1762.595, 15.0, 0.042851, 22552930.0, 57.0, 50.0, 182.1, 56.0, 4483873.0, 46.0, 12870059.0, 58.0, 0.0197, 53.0, 42.0, 0.007124, 143.38, 768])
remember_rows.append( [0.019711, 57.0, 5.0, 111.67, 18215680.0, 1763.97, 15.0, 0.043663999999999994, 22583114.0, 57.0, 48.0, 182.1, 56.0, 4487441.0, 45.0, 12885757.0, 58.0, 0.019485, 53.0, 42.0, 0.007034, 143.3498, 770])
remember_rows.append( [0.019655, 57.0, 5.0, 111.65, 18267550.0, 1765.345, 15.0, 0.044478, 22613848.0, 57.0, 48.0, 182.09, 56.0, 4494421.0, 45.0, 12895241.0, 58.0, 0.019415, 53.0, 42.0, 0.006854, 143.34, 771])
remember_rows.append( [0.018815, 57.0, 5.0, 111.58, 18323420.0, 1763.11, 15.0, 0.043155, 22678559.0, 57.0, 49.0, 181.94, 56.0, 4504769.0, 45.0, 12932586.0, 58.0, 0.018384, 53.0, 42.0, 0.006222, 143.195, 772])
remember_rows.append( [0.022174999999999997, 57.0, 4.0, 111.875, 19170706.0, 1766.75, 15.0, 0.045309, 23660207.0, 57.0, 48.0, 182.54, 56.0, 4672407.0, 45.0, 13512602.0, 58.0, 0.019415, 53.0, 42.0, 0.008883, 143.34, 795])
remember_rows.append( [0.022455, 57.0, 4.0, 111.9, 19194281.0, 1767.3802, 15.0, 0.045682, 23701466.0, 57.0, 48.0, 182.59, 56.0, 4677798.0, 45.0, 13533989.0, 58.0, 0.019487, 53.0, 42.0, 0.009108, 143.35, 796])
remember_rows.append( [0.022511, 57.0, 4.0, 111.92, 19239698.0, 1769.0, 15.0, 0.046639999999999994, 23746255.0, 57.0, 51.0, 182.6, 56.0, 4688570.0, 48.0, 13551695.0, 58.0, 0.019415, 53.0, 42.0, 0.009288, 143.34, 797])
remember_rows.append( [0.022847, 57.0, 4.0, 111.985, 19277472.0, 1769.045, 15.0, 0.04666699999999999, 23784796.0, 57.0, 51.0, 182.66, 56.0, 4697969.0, 48.0, 13573367.0, 58.0, 0.0197, 53.0, 42.0, 0.009875, 143.38, 798])
remember_rows.append( [0.022679, 57.0, 5.0, 111.94, 19343243.0, 1767.72, 15.0, 0.045883, 23834864.0, 57.0, 51.0, 182.63, 56.0, 4707356.0, 47.0, 13603559.0, 58.0, 0.019131, 53.0, 42.0, 0.009469, 143.3, 799])

remember_rows.append( [0.023462999999999998, 57.0, 5.0, 112.0197, 19379591.0, 1768.665, 15.0, 0.046442, 23863100.0, 57.0, 51.0, 182.77, 56.0, 4712747.0, 47.0, 13632426.0, 58.0, 0.019415, 53.0, 42.0, 0.010188, 143.34, 800])
remember_rows.append( [0.023014999999999997, 57.0, 5.0, 111.99, 19412315.0, 1768.82, 15.0, 0.046534000000000006, 23906590.0, 57.0, 49.0, 182.69, 56.0, 4719217.0, 45.0, 13658666.0, 58.0, 0.018989, 53.0, 42.0, 0.00992, 143.28, 801])
remember_rows.append( [0.023183, 57.0, 5.0, 111.99, 19438108.0, 1768.77, 15.0, 0.046504000000000004, 23934949.0, 57.0, 49.0, 182.72, 56.0, 4723063.0, 45.0, 13672900.0, 58.0, 0.019131, 53.0, 42.0, 0.00992, 143.3, 802])
remember_rows.append( [0.023014999999999997, 57.0, 5.0, 111.97, 19474000.0, 1767.0, 15.0, 0.045457, 23983108.0, 57.0, 49.0, 182.6901, 56.0, 4731228.0, 46.0, 13708675.0, 58.0, 0.018703, 53.0, 42.0, 0.009739, 143.2399, 803])
remember_rows.append( [0.023237999999999998, 57.0, 5.0, 111.9411, 19503695.0, 1767.11, 15.0, 0.045522, 24021968.0, 57.0, 49.0, 182.7299, 56.0, 4735503.0, 46.0, 13722844.0, 58.0, 0.018349, 53.0, 42.0, 0.009479, 143.19, 804])
remember_rows.append( [0.022963, 57.0, 5.0, 111.94, 19531749.0, 1766.5, 15.0, 0.045161, 24056729.0, 57.0, 50.0, 182.6807, 56.0, 4740840.0, 46.0, 13745487.0, 58.0, 0.018420000000000002, 53.0, 42.0, 0.009469, 143.2, 805])
remember_rows.append( [0.022847, 57.0, 5.0, 111.86, 19562510.0, 1766.21, 15.0, 0.044989999999999995, 24084321.0, 57.0, 50.0, 182.66, 56.0, 4745164.0, 46.0, 13768895.0, 58.0, 0.01778, 53.0, 42.0, 0.008747, 143.11, 806])
remember_rows.append( [0.022511, 57.0, 5.0, 111.8, 19593261.0, 1766.29, 15.0, 0.045037, 24138553.0, 57.0, 50.0, 182.6, 56.0, 4749998.0, 46.0, 13790412.0, 58.0, 0.017211, 53.0, 42.0, 0.008206, 143.03, 808])
remember_rows.append( [0.022462, 57.0, 5.0, 111.8067, 19618315.0, 1765.0, 15.0, 0.044273999999999994, 24192719.0, 57.0, 50.0, 182.5913, 56.0, 4757462.0, 46.0, 13827087.0, 58.0, 0.017069, 53.0, 42.0, 0.008267, 143.0101, 809])
remember_rows.append( [0.022735, 57.0, 5.0, 111.79, 19684066.0, 1765.46, 15.0, 0.044546, 24227951.0, 57.0, 49.0, 182.64, 56.0, 4766707.0, 45.0, 13860247.0, 58.0, 0.017230000000000002, 53.0, 42.0, 0.008116, 143.0327, 810])

remember_rows.append( [0.022566000000000003, 57.0, 5.0, 111.75, 19732249.0, 1765.4705, 15.0, 0.044551999999999994, 24268849.0, 57.0, 49.0, 182.6099, 56.0, 4776271.0, 45.0, 13893914.0, 58.0, 0.016279, 53.0, 42.0, 0.007755, 142.899, 811])
