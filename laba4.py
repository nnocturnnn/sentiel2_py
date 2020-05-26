import zipfile
import os
import sys
import subprocess
from sentinelhub import AwsProductRequest

         

product_id = 'S2A_MSIL2A_20190821T085601_N0213_R007_T36UUB_20190821T115206'
product_id1 = 'S2A_MSIL2A_20190821T085601_N0213_R007_T36UUB_20190821T115206'
data_folder = r'C:\Users\sido1\Desktop\musor4laba'


sentid = input('choise your sentiel id to dowload data : ')
sentkey = input('choise your sentiel key to dowload data : ')
subprocess.call('sentinelhub.config --instance_id '  + sentid + '--aws_secret_access_key ' + sentkey)

try:
	product_request = AwsProductRequest(product_id=product_id, data_folder=data_folder, safe_format=True)
	product_request.save_data()
	product_request1 = AwsProductRequest(product_id=product_id1, data_folder=data_folder, safe_format=True)
	product_request.save_data()
except:
	subprocess.call('sentinelhub.aws --product '  + product_id)
	subprocess.call('sentinelhub.aws --product '  + product_id1)

product_idpath = data_folder  + '\\' + product_id
product_idpath1 = data_folder + '\\' + product_id1
zip2 = zipfile.ZipFile(product_idpath + '.zip')
zip2.extractall(product_idpath)
zip2.close()

zip3 = zipfile.ZipFile(product_idpath1 + '.zip')
zip3.extractall(product_idpath1)
zip3.close()
iterfilename = 1
gm = os.path.join('C:\\','Program Files','QGIS 3.12','apps','Python37','Scripts','gdal_merge.py')
sys.path.append('C:\\Program Files\\QGIS 3.12\\bin')
listdir = os.listdir(path=r"C:\Users\sido1\Desktop\musor4laba\S2A_MSIL2A_20190821T085601_N0213_R007_T36UUA_20190821T115206.SAFE\GRANULE\L2A_T36UUA_A021740_20190821T085815\IMG_DATA")
for i in listdir:
	firstlist = os.listdir(path="C:\\Users\\sido1\\Desktop\\musor4laba\\S2A_MSIL2A_20190821T085601_N0213_R007_T36UUA_20190821T115206.SAFE\\GRANULE\\L2A_T36UUA_A021740_20190821T085815\\IMG_DATA\\" + i)
	infrapath = 'C:/Users/sido1/Desktop/musor4laba/S2A_MSIL2A_20190821T085601_N0213_R007_T36UUA_20190821T115206.SAFE/GRANULE/L2A_T36UUA_A021740_20190821T085815/IMG_DATA/' + i
	os.chdir(infrapath)
	for i in firstlist:
		newname = i.replace('jp2', 'tif')
		print('gdal_translate ' + i  + ' '  + newname)
		subprocess.call('gdal_translate ' + i  + ' '  + newname)

	firstlisttif = os.listdir(path="C:\\Users\\sido1\\Desktop\\musor4laba\\S2A_MSIL2A_20190821T085601_N0213_R007_T36UUA_20190821T115206.SAFE\\GRANULE\\L2A_T36UUA_A021740_20190821T085815\\IMG_DATA\\" + i)
	needtif = []
	for i in firstlisttif:
		if i.find('.tif') > -1 and (i.find('B02') > -1 or i.find('B03') > -1 or i.find('B04') > -1 or i.find('B08') > -1):
			needtif.append(i)
	merge_command = ["python", gm, "-o",str(iterfilename) + "merged.tif" , needtif[0], needtif[1], needtif[2], needtif[3]]
	os.system('mv ' + str(iterfilename) + 'merged.tif ' + 'C:\\Users\\sido1\\Desktop\\musor4laba')
	iterfilename += 1
	subprocess.call(merge_command,shell=True)
	os.chdir('C:\\Users\\sido1\\Desktop\\musor4laba')
	subprocess.call('gdalwarp -t_srs EPSG:4326 ' + str(iterfilename) + 'merged.tif ' + str(iterfilename) + 'merged4326.tif')
	listmergetif =  os.listdir(path='C:\\Users\\sido1\\Desktop\\musor4laba')
	canal4input = ''
	for i in listmergetif:
		if i.find('merged4326.tif') > -1:
			canal4input += ' ' + i
	subprocess.call('gdalwarp –of TIFF –ot TIFF –srcnodata  –dstnodata '  + canal4input  + ' ' + '4chanel.tif')

listdir2 = os.listdir(path=r"C:\Users\sido1\Desktop\musor4laba\S2A_MSIL2A_20190821T085601_N0213_R007_T36UUB_20190821T115206.SAFE\GRANULE\L2A_T36UUB_A021740_20190821T085815\IMG_DATA")
for i in listdir2:
	secondlist = os.listdir(path="C:\\Users\\sido1\\Desktop\\musor4laba\\S2A_MSIL2A_20190821T085601_N0213_R007_T36UUB_20190821T115206.SAFE\\GRANULE\\L2A_T36UUB_A021740_20190821T085815\\IMG_DATA\\"  + i)
	infrapath2 = 'C:/Users/sido1/Desktop/musor4laba/S2A_MSIL2A_20190821T085601_N0213_R007_T36UUB_20190821T115206.SAFE/GRANULE/L2A_T36UUB_A021740_20190821T085815/IMG_DATA/'  + i
	os.chdir(infrapath2)
	for i in secondlist:
		newname = i.replace('jp2', 'tif')
		print('gdal_translate ' + i  + ' '  + newname)
		subprocess.call('gdal_translate ' + i  + ' '  + newname)

	secondlisttif = os.listdir(path="C:\\Users\\sido1\\Desktop\\musor4laba\\S2A_MSIL2A_20190821T085601_N0213_R007_T36UUB_20190821T115206.SAFE\\GRANULE\\L2A_T36UUB_A021740_20190821T085815\\IMG_DATA\\" + i)
	needtif2 = []
	for i in secondlisttif:
		if i.find('.tif') > -1 and (i.find('B02') > -1 or i.find('B03') > -1 or i.find('B04') > -1 or i.find('B08') > -1):
			needtif2.append(i)
	merge_command = ["python", gm, "-o", str(iterfilename) + "merged.tif", needtif2[0], needtif2[1], needtif2[2], needtif2[3]]
	os.system('mv ' + str(iterfilename) + 'merged.tif ' + 'C:\\Users\\sido1\\Desktop\\musor4laba')
	iterfilename += 1
	subprocess.call(merge_command,shell=True)
	os.chdir('C:\\Users\\sido1\\Desktop\\musor4laba')
	subprocess.call('gdalwarp -t_srs EPSG:4326 ' + str(iterfilename) + 'merged.tif ' + str(iterfilename) + 'merged4326.tif')
	listmergetif2 =  os.listdir(path='C:\\Users\\sido1\\Desktop\\musor4laba')
	canal4input2 = ''
	for i in listmergetif2:
		if i.find('merged4326.tif') > -1:
			canal4input2 += ' ' + i
	subprocess.call('gdalwarp –of TIFF –ot TIFF –srcnodata  –dstnodata '  + canal4input2  + ' ' + '4chanel.tif')