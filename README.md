# Photo2KML v2.1 使用说明
# Photo2KML v2.1 User Guide


## 中文说明

### 简介

Photo2KML 是一个离线照片 GPS 轨迹生成工具。

它可以读取照片中的 EXIF GPS 信息，并生成：

- KML 文件（Google Earth）
- GPX 文件（GPS轨迹）
- CSV 文件（Excel数据分析）

所有处理均在本地完成，不会上传任何照片。


---

## 使用方法

### 第一步：准备照片

将 `Photo2KML.exe` 放入照片所在文件夹。

例如：
旅行照片

│
├── IMG001.jpg
├── IMG002.jpg
├── IMG003.jpg
└── Photo2KML.exe



支持：

- JPG / JPEG
- 包含GPS信息的照片


注意：

照片必须包含 GPS 位置信息。

手机拍摄照片通常默认包含 GPS。

如果照片没有GPS信息，将不会生成对应地图点。


---

### 第二步：运行程序

双击：
Photo2KML.exe



程序会自动：

1. 扫描当前文件夹及子文件夹中的照片
2. 读取照片 EXIF GPS 信息
3. 按拍摄时间排序
4. 生成地图文件


处理时间取决于照片数量。

几千张照片通常需要几十秒。


---

### 第三步：查看结果

程序完成后，会生成：
Photo2KML_Output
│
├── Photos.kml
├── Photos.gpx
├── PhotoLocations.csv
└── Photo2KML.log



文件说明：

### Photos.kml

用于：

- Google Earth
- 奥维互动地图
- QGIS


显示：

- 照片位置
- 拍摄时间
- GPS轨迹


### Photos.gpx

用于：

- GPS软件
- GIS软件
- 轨迹分析工具


### PhotoLocations.csv

可以使用：

- Microsoft Excel
- WPS Office

查看：

- 文件名
- 时间
- 纬度
- 经度
- 相机型号


### Photo2KML.log

运行日志。

包含：

- 扫描数量
- 有效GPS照片数量
- 错误信息


---

## 注意事项

1. 照片必须包含 GPS 信息。

2. 程序不会修改原始照片。

3. 所有数据均离线处理。

4. 第一次处理大量照片可能需要较长时间。


------------------------------------------------------------------------------------------

# English Guide


## Introduction

Photo2KML is an offline photo GPS track generator.

It extracts GPS information from photo EXIF metadata and generates:

- KML files for Google Earth
- GPX GPS tracks
- CSV location data


All processing is performed locally.
No photos are uploaded.


---

## How to Use


### Step 1: Prepare Photos

Copy `Photo2KML.exe` into your photo folder.


Example:
Travel Photos
│
├── IMG001.jpg
├── IMG002.jpg
├── IMG003.jpg
└── Photo2KML.exe



Supported:

- JPG / JPEG photos
- Photos containing EXIF GPS information


Note:

Only photos with GPS metadata can be displayed on the map.


---

### Step 2: Run the Program

Double-click:


Photo2KML.exe



The program will automatically:

1. Scan photos in the current folder and subfolders
2. Extract EXIF GPS coordinates
3. Sort photos by shooting time
4. Generate map files


Processing time depends on the number of photos.


---

### Step 3: Check Output Files


After completion:


Photo2KML_Output
│
├── Photos.kml
├── Photos.gpx
├── PhotoLocations.csv
└── Photo2KML.log



### Photos.kml

Compatible with:

- Google Earth
- Ovi Maps
- QGIS


Contains:

- Photo locations
- Shooting time
- GPS route


### Photos.gpx

Compatible with:

- GPS applications
- GIS software
- Track analysis tools


### PhotoLocations.csv

Can be opened with:

- Microsoft Excel
- WPS Office


Contains:

- File name
- Date and time
- Latitude
- Longitude
- Camera model


### Photo2KML.log

Execution log including:

- Number of scanned photos
- GPS photo count
- Error information


---

## Notes

1. Photos must contain GPS metadata.

2. Original photos are never modified.

3. All processing is completely offline.

4. Large photo collections may require additional processing time.
