import os
import subprocess
from microWebSrv import MicroWebSrv
import json


@MicroWebSrv.route('/monitor_mode_disable')
def _httpHandlerMonitorDisable(httpClient, httpResponse) :
    cmd = ['/etc/local.d/monitor_mode_disable.sh']
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    response = []

    for line in process.stdout:
        print(line)
        response.append(str(line))

    process.wait()

    httpResponse.WriteResponseJSONOk(obj={'response': response})

@MicroWebSrv.route('/monitor_mode_enable')
def _httpHandlerMonitorEnable(httpClient, httpResponse) :
    cmd = ['/etc/local.d/monitor_mode_enable.sh']
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    response = []

    for line in process.stdout:
        print(line)
        response.append(str(line))

    process.wait()

    httpResponse.WriteResponseJSONOk(obj={'response': response})

@MicroWebSrv.route('/show_network_interfaces')
def _httpHandleGetShowNetworkInterfaces(httpClient, httpResponse) :
    cmd = ['/etc/local.d/wifi_interfaces.sh']
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    response = []

    for line in process.stdout:
        print(line)
        response.append(str(line))

    process.wait()

    httpResponse.WriteResponseJSONOk(obj={'response': response})

@MicroWebSrv.route('/wifi_networks')
def _httpHandlerWifiNetworks(httpClient, httpResponse) :
    cmd = ['/etc/local.d/scan_wifi_networks.sh']
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    response = []

    for line in process.stdout:
        print(line)
        response.append(str(line))

    process.wait()
    httpResponse.WriteResponseJSONOk(obj={'response': response, 'errors': errors})
# ----------------------------------------------------------------------------

def _acceptWebSocketCallback(webSocket, httpClient) :
	print("WS ACCEPT")
	webSocket.RecvTextCallback   = _recvTextCallback
	webSocket.RecvBinaryCallback = _recvBinaryCallback
	webSocket.ClosedCallback 	 = _closedCallback

def _recvTextCallback(webSocket, msg) :
	print("WS RECV TEXT : %s" % msg)
	webSocket.SendText("Reply for %s" % msg)

def _recvBinaryCallback(webSocket, data) :
	print("WS RECV DATA : %s" % data)

def _closedCallback(webSocket) :
	print("WS CLOSED")

# ----------------------------------------------------------------------------

srv = MicroWebSrv(webPath='www/')
srv.MaxWebSocketRecvLen = 256
srv.WebSocketThreaded = False
srv.AcceptWebSocketCallback = _acceptWebSocketCallback
srv.Start()
