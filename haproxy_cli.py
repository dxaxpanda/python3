#!/usr/bin/env python
# -*- coding: utf-8 -*-


HEADER_LIST = 'pxname,svname,qcur,qmax,scur,smax,slim,stot,bin,bout,dreq,dresp,ereq,econ,eresp,wretr,wredis,status,weight,act,bck,chkfail,chkdown,lastchg,downtime,qlimit,pid,iid,sid,throttle,lbtot,tracked,type,rate,rate_lim,rate_max,check_status,check_code,check_duration,hrsp_1xx,hrsp_2xx,hrsp_3xx,hrsp_4xx,hrsp_5xx,hrsp_other,hanafail,req_rate,req_rate_max,req_tot,cli_abrt,srv_abrt,comp_in,comp_out,comp_byp,comp_rsp,lastsess,last_chk,last_agt,qtime,ctime,rtime,ttime,agent_status,agent_code,agent_duration,check_desc,agent_desc,check_rise,check_fall,check_health,agent_rise,agent_fall,agent_health,addr,cookie,mode,algo,conn_rate,conn_rate_max,conn_tot,intercepted,dcon,dses'


def parser(stats):
    list_length = stats.split(',')

    field_name_list = HEADER_LIST.split(',')

    haproxy_dict = {}


    index = 0

    for item in list_length:
        field_name = field_name_list[index]
        haproxy_dict[field_name] = item

        index++1
    return haproxy_dict

def test_haproxy_stats():

    stat_output =
