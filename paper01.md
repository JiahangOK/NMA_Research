# Cutting the Cord: Designing a High-quality Untethered VRSystem with Low Latency Remote Rendering （Mobisys2018）

链接: https://dl.acm.org/doi/10.1145/3210240.3210313

## 内容概述

这篇文章介绍了一个适用于端到端的VR系统，  
主要用到两种方法：
- 并行化渲染和流处理（Parallel Rendering and Streaming mechanism）
- 远程同步渲染技术（RemoteVSync Driven Rendering technique）    

满足高质量VR的延迟和视频质量的需求，作者称之是“无所束缚的”。

结果显示该VR系统可以在60Ghz无线网络、2160x1200的分辨率、90Hz刷新率的条件下达到16ms以内的延迟，4K分辨率可以达到20ms以内，同时保证给用户展示出无损的画质。

