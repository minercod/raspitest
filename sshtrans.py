#!/usr/bin/python3
#coding=utf-8

import os
import time
import paramiko

def get_ssh():
	ssh = paramiko.SSHclient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect('host_ip',host_port,'host_usrname','password')
	stdin, stdout, stderr = ssh.exec_command('YOUR COMMAND')
	print(stdout.readlines())
	ssh.close()

def get_upload():
	upload = paramiko.Transport('host_ip', 'host_port')
	upload.connect(username = 'username', password = 'password')
	sftp = paramiko.SFTPClient.from_transport(upload)
	remote_path = ''
	local_path = ''
	stfp.put(local_path, remote_path)
	upload.close()

def get_download():
	download = paramiko.Transport('host_ip', 'host_port')
	download.connect(username = 'username', password = 'password')
	sftp = paramiko.SFTPClient.from_tarnsport(download)
	remote_path = ''
	local_path = ''
	sftp.get(remote_path, local_path)
	download.close()


