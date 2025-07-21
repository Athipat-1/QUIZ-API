## PROJECT STRUCTURE ##

  QUIZ API
   -api1
    -api1.py
    -Dockerfile
    -requirements.txt
  -api2
    -api2.py
    -Dockerfile
    -requirements.txt
  -docker-compose.yml
  -README.md

---------------------------------------------------------------------------------------------

## PREPARE ##
  ใช้คำสั่ง git cloneตามด้วยhttps://github.com/Athipat-1/QUIZ-API 
  เพื่อโหลดโค้ดลง vscode

  โหลด Docker desktop [https://www.docker.com/get-started/]
  ใช้คำสั่งเพื่อ Deploy (docker-compose up --build)        
  เช็ค Docker (Docker ps)
  Example:ถ้าขึ้น
  CONTAINER ID   IMAGE   COMMAND    CREATED   STATUS    PORTS     NAMES
  แล้วมีข้อมูล 
  หมายความว่าใช้ได้แล้ว จะขึ้นประมาณนี้ https://ibb.co/Zz7jzCNY

---------------------------------------------------------------------------------------------

## TEST ##
เทสในCMDใช้คำสั่ง:curl http://localhost:4321/sawasdeekub
เทสในBROWSERใช้คำสั่ง:http://localhost:4321/sawasdeekub

---------------------------------------------------------------------------------------------

## OUTPUT ## 

{
  "message_from_api2": "sawasdeekub from API2!"
}

---------------------------------------------------------------------------------------------
