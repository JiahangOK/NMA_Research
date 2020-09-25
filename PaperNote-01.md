# Cutting the Cord: Designing a High-quality Untethered VR System with Low Latency Remote Rendering （Mobisys2018）

链接: https://dl.acm.org/doi/10.1145/3210240.3210313

## 内容概述

这篇文章介绍了一个适用于端到端的VR系统，  
主要用到两种方法：
- 并行化渲染和流处理（Parallel Rendering and Streaming mechanism）
- 远程垂直同步渲染技术（Remote VSync Driven Rendering technique）    

在无线网络条件下，满足高质量VR的延迟和视频质量的需求，因此作者称之是“无所束缚的”,"Cutting the Cord"这个标题也是蛮生动形象的。

结果显示该VR系统可以在60Ghz无线网络、2160x1200的分辨率、90Hz刷新率的条件下达到16ms以内的延迟，4K分辨率可以达到20ms以内，同时保证给用户展示出无损的画质。

## 背景
VR的设备主要分为两种，一种是**结合式**的，另一种是**独立式**的。

- **结合式VR**需要将头戴设备（*Head Mounted Display, HMD*）和PC连接起来，头戴设备通过USB线将传感器数据传输给PC，然后PC通过HDMI线将渲染的画面传回给头戴设备，这种方式可以是VR的画面质量更高清保真。

- **独立式VR**只是在单独一个设备上对画面进行操作，这种方式摆脱了“绳子的束缚”。

## 存在的问题

- **结合式VR**有“绳索的束缚”，用户行动不方便，甚至有安全隐患（比如被绳子缠绕脖子就麻烦了。。。hhh）
- **独立式VR**计算资源有限，没法做到高质量的画面渲染，有的人尝试用无线传输的方式将一些计算任务迁移到PC上，然而延迟会对画面帧率造成影响，使VR用户产生眩晕的感觉，严重影响用户体验。


