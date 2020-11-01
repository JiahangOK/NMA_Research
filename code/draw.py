# -*- coding:utf-8 -*-
from matplotlib.pylab import *
import numpy as np
import scipy.io as sio
import matplotlib as mpl
import matplotlib.ticker as ticker

# 全局参数设置
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
matplotlib.rcParams['font.serif'] = ['Times New Roman']
# plt.rc('xtick', labelsize='x-small')
# plt.rc('ytick', labelsize='x-small')
csfont = {'fontname': 'Comic Sans MS'}
hfont = {'fontname': 'Helvetica'}
tfont = {'fontname': 'Times New Roman'}
color_arr = np.array([[228, 26, 28], [55, 126, 184], [77, 175, 74], [
                     152, 78, 163], [255, 127, 0], [27, 158, 119]])
color_arr = color_arr * 1.0 / 255
color_arr = color_arr.tolist()
hatches = ['///', '+++', 'xxx', '\\\\\\', '---', 'xxx']
params = {
    'axes.labelsize': 8,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': False,
    'axes.labelsize': 12,
    'figure.figsize': [4.5, 3]
}
rcParams.update(params)

def jpeg_x_quality_y_ssim():
    # data
    quality = ['0', '20', '40', '60', '80', '85', '90', '100']
    avg_ssim = []
    for q in quality:
        f_name = "data/jpeg_encode_{}_2688.log".format(q)
        ssims = []
        with open(f_name, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line: 
                l = line.split('\n')[0]
                ssims.append(float(l.split(',')[3]))
                line = f.readline() 
        avg_ssim.append(np.mean(ssims))

    # draw
    _, ax= plt.subplots(1, 1, figsize=(8, 6))
    ax.yaxis.grid(True, linestyle='--', color='gray', lw=1.)
    x = np.arange(len(quality))
    ax.bar(x, avg_ssim, width=0.3, color='none', edgecolor=color_arr[0], 
        hatch=hatches[0], lw=2., label='JPEG')

    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7])
    ax.set_xticklabels(quality)
    ax.set_yticks([0.7, 0.8, 0.9, 0.98, 1.0])
    ax.set_xlabel('Quality')
    ax.set_ylabel('SSIM')
    ax.set_ylim(0.7, 1)
    ax.legend()
    plt.savefig('figs/jpeg_x_quality_y_ssim.png')
    plt.show()

def hevc_x_qp_y_ssim():
    # data
    quality = ['50', '40', '30', '20', '10', '0']
    avg_ssim = []
    for q in quality:
        f_name = "data/encoder_time_2688_{}.log".format(q)
        ssims = []
        with open(f_name, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line: 
                l = line.split('\n')[0]
                ssims.append(float(l.split(',')[4]))
                line = f.readline() 
        avg_ssim.append(np.mean(ssims))

    # draw
    _, ax= plt.subplots(1, 1, figsize=(8, 6))
    ax.yaxis.grid(True, linestyle='--', color='gray', lw=1.)
    x = np.arange(len(quality))
    ax.bar(x, avg_ssim, width=0.3, color='none', edgecolor=color_arr[2], 
        hatch=hatches[0], lw=2., label='HEVC')

    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(quality)
    ax.set_yticks([0.7, 0.8, 0.9, 0.98, 1.0])
    ax.set_xlabel('qp')
    ax.set_ylabel('SSIM')
    ax.set_ylim(0.7, 1)
    ax.legend()
    plt.savefig('figs/hevc_x_qp_y_ssim.png')
    plt.show()

def x_encodetype_y_filesize_time():
    # qp=10 quality=85 avg_ssim>0.98
    # data
    quality = ['JPEG(quality=85)', 'HEVC_P(qp=10)', 'HEVC(qp=10)','HEVC_I(qp=10)']
    avg_file_size = []
    avg_encode_time = []
    
    with open('data/jpeg_encode_85_2688.log', 'r', encoding='utf-8') as f:
        line = f.readline()
        file_size = []
        times = []
        while line: 
            l = line.split('\n')[0]
            file_size.append(float(l.split(',')[2]) / 1000)
            times.append(float(l.split(',')[1]))
            line = f.readline() 
        avg_file_size.append(np.mean(file_size))
        avg_encode_time.append(np.mean(times))

    with open('data/encoder_size_2688_10.log', 'r', encoding='utf-8') as f:
        line = f.readline()
        file_size = []
        file_size_i = []
        file_size_p = []
        while line: 
            l = line.split('\n')[0]
            if int(l.split(',')[1]) != -1:
                file_size.append(float(l.split(',')[2]) / 1000)
                if int(l.split(',')[0]) % 10 == 0:
                    file_size_i.append(float(l.split(',')[2]) / 1000)
                else:
                    file_size_p.append(float(l.split(',')[2]) / 1000)
            line = f.readline() 
        avg_file_size.append(np.mean(file_size_p))
        avg_file_size.append(np.mean(file_size))
        avg_file_size.append(np.mean(file_size_i))
       
    with open('data/encoder_time_2688_10.log', 'r', encoding='utf-8') as f:
        line = f.readline()
        times = []
        times_i = []
        times_p = []
        while line: 
            l = line.split('\n')[0]
            times.append(float(l.split(',')[3]))
            if int(l.split(',')[0]) % 10 == 0:
                times_i.append(float(l.split(',')[3]))
            else:
                times_p.append(float(l.split(',')[3]))
            line = f.readline() 
        avg_encode_time.append(np.mean(times_p))
        avg_encode_time.append(np.mean(times))
        avg_encode_time.append(np.mean(times_i))
        
    
    # draw
    fig, ax= plt.subplots(1, 1, figsize=(8, 6))
    ax.yaxis.grid(True, linestyle='--', color='gray', lw=1.)
    x = np.arange(len(quality))
    width = 0.36
    ax.bar(x-width/2, avg_file_size, width=0.3, color='none', edgecolor=color_arr[0], 
        hatch=hatches[0], lw=2., label='Encoded Size')
    ax2=ax.twinx()
    ax2.bar(x+width/2, avg_encode_time, width=0.3, color='none', edgecolor=color_arr[1], 
        hatch=hatches[2], lw=2., label='Encode Time')

    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(quality)
    ax.set_xlabel('Encode Method')
    ax.set_ylabel('Encoded File Size(KB)')
    ax2.set_ylabel('Encode Time (ms)')
    fig.legend(loc="best", bbox_transform=ax.transAxes)
    plt.savefig('figs/x_encodetype_y_filesize.png')
    plt.show()

def x_slide_y_f1_latency():
    # data
    sliding = ['1x1', '2x1', '4x1', '6x1', '8x1', '10x1']
    f1 = [0.2963, 0.3326, 0.3807, 0.4154, 0.4152, 0.4165]
    avg_latency = []

    for sl in sliding: 
        receive_time = {}
        send_time = {}
        with open("data/E2E/detect_start_time_{}.txt".format(sl), 'r', encoding='utf-8') as f:
            line = f.readline()
            while line: 
                l = line.split('\n')[0]
                frame_id = l.split(',')[0]
                time = int(l.split(',')[1])
                receive_time[frame_id] = time
                line = f.readline() 
        with open("data/E2E/encoder_time_2688_10_{}.log".format(sl), 'r', encoding='utf-8') as f:
            line = f.readline()
            while line: 
                l = line.split('\n')[0]
                frame_id = l.split(',')[0]
                time = int(l.split(',')[2])
                send_time[frame_id] = time
                line = f.readline() 
        
        print(sl)
        print(receive_time)
        print(send_time)
        latency = []
        for key in receive_time:
            if(receive_time[key]-send_time[key] < 200 and receive_time[key]-send_time[key] > 100): # 过滤掉不正常的数据
                latency.append(receive_time[key]-send_time[key])
        print(latency)
        avg_latency.append(np.mean(latency))
    print(avg_latency)
    # draw
    fig, ax= plt.subplots(1, 1, figsize=(8, 6))
    ax.yaxis.grid(True, linestyle='--', color='gray', lw=1.)
    x = np.arange(len(sliding))
    width = 0.36
    ax.bar(x-width/2, f1, width=0.3, color='none', edgecolor=color_arr[4], 
        hatch=hatches[0], lw=2., label='F1 Score')
    ax2=ax.twinx()
    ax2.bar(x+width/2, avg_latency, width=0.3, color='none', edgecolor=color_arr[5], 
        hatch=hatches[2], lw=2., label='End-to-End Latency')

    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(sliding)
    # ax.set_yticks([0.7, 0.8, 0.9, 0.98, 1.0])
    ax.set_xlabel('Sliding Methods')
    ax.set_ylabel('F1 Score')
    ax.set_ylim(0.25, 0.5)
    ax2.set_ylim(100, 200)
    ax2.set_ylabel('End-to-End Latency (ms)')
    fig.legend(loc="best", bbox_transform=ax.transAxes)
    plt.savefig('figs/x_slide_y_f1_latency.png')
    plt.show()

if __name__ == "__main__":
    # JPEG qualityh和SSIM的关系
    # jpeg_x_quality_y_ssim()

    # HEVC qp和SSIM的关系
    # hevc_x_qp_y_ssim()

    # SSIM相同，压缩文件大小，压缩时间比较
    x_encodetype_y_filesize_time()

    # 不同分片的检测精度变化
    # x_slide_y_f1_latency()

    