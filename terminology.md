# 术语中英文对照表

## 第一章：RV64 裸机应用

| 中文       | 英文                                  | 出现章节                                                                            |
|----------|-------------------------------------|---------------------------------------------------------------------------------|
| 执行环境     | Execution Environment               | [应用程序运行环境与平台支持](chapter1/1app-ee-platform.md#term-execution-environment)        |
| 系统调用     | System Call                         | [应用程序运行环境与平台支持](chapter1/1app-ee-platform.md#term-system-call)                  |
| 指令集体系结构  | ISA, Instruction Set Architecture   | [应用程序运行环境与平台支持](chapter1/1app-ee-platform.md#term-isa)                          |
| 抽象       | Abstraction                         | [应用程序运行环境与平台支持](chapter1/1app-ee-platform.md#term-abstraction)                  |
| 平台       | Platform                            | [应用程序运行环境与平台支持](chapter1/1app-ee-platform.md#term-platform)                     |
| 目标三元组    | Target Triplet                      | [应用程序运行环境与平台支持](chapter1/1app-ee-platform.md#term-target-triplet)               |
| 裸机平台     | Bare-Metal                          | [应用程序运行环境与平台支持](chapter1/1app-ee-platform.md#term-bare-metal)                   |
| 交叉编译     | Cross Compile                       | [移除标准库依赖](chapter1/2remove-std.md#term-cross-compile)                           |
| 物理地址     | Physical Address                    | [内核第一条指令（原理篇）](chapter1/3first-instruction-in-kernel1.md#term-physical-address) |
| 物理内存     | Physical Memory                     | [内核第一条指令（原理篇）](chapter1/3first-instruction-in-kernel1.md#term-physical-memory)  |
| 引导加载程序   | Bootloader                          | [内核第一条指令（原理篇）](chapter1/3first-instruction-in-kernel1.md#term-bootloader)       |
| 控制流      | Control Flow                        | [为内核支持函数调用](chapter1/5support-func-call.md#term-control-flow)                   |
| 函数调用     | Function Call                       | [为内核支持函数调用](chapter1/5support-func-call.md#term-function-call)                  |
| 源寄存器     | Source Register                     | [为内核支持函数调用](chapter1/5support-func-call.md#term-source-register)                |
| 立即数      | Immediate                           | [为内核支持函数调用](chapter1/5support-func-call.md#term-immediate)                      |
| 目标寄存器    | Destination Register                | [为内核支持函数调用](chapter1/5support-func-call.md#term-destination-register)           |
| 伪指令      | Pseudo Instruction                  | [为内核支持函数调用](chapter1/5support-func-call.md#term-pseudo-instruction)             |
| 上下文      | Context                             | [为内核支持函数调用](chapter0/3os-hw-abstract.md#term-context)                           |
| 活动记录     | Activation Record                   | [为内核支持函数调用](chapter1/5support-func-call.md#term-activation-record)              |
| 保存/恢复    | Save/Restore                        | [为内核支持函数调用](chapter1/5support-func-call.md#term-save-restore)                   |
| 被调用者保存   | Callee-Saved                        | [为内核支持函数调用](chapter1/5support-func-call.md#term-callee-saved)                   |
| 调用者保存    | Caller-Saved                        | [为内核支持函数调用](chapter1/5support-func-call.md#term-caller-saved)                   |
| 开场白      | Prologue                            | [为内核支持函数调用](chapter1/5support-func-call.md#term-prologue)                       |
| 收场白      | Epilogue                            | [为内核支持函数调用](chapter1/5support-func-call.md#term-epilogue)                       |
| 调用规范     | Calling Convention                  | [为内核支持函数调用](chapter1/5support-func-call.md#term-calling-convention)             |
| 栈/栈指针/栈帧 | Stack/Stack Pointer/Stackframe      | [为内核支持函数调用](chapter1/5support-func-call.md#term-stack)                          |
| 后入先出     | LIFO, Last In First Out             | [为内核支持函数调用](chapter1/5support-func-call.md#term-lifo)                           |
| 段        | Section                             | [为内核支持函数调用](chapter1/3first-instruction-in-kernel1.md#term-section)             |
| 内存布局     | Memory Layout                       | [为内核支持函数调用](chapter1/3first-instruction-in-kernel1.md#term-memory-layout)       |
| 堆        | Heap                                | [为内核支持函数调用](chapter1/3first-instruction-in-kernel1.md#term-heap)                |
| 编译器      | Compiler                            | [为内核支持函数调用](chapter1/3first-instruction-in-kernel1.md#term-compiler)            |
| 汇编器      | Assembler                           | [为内核支持函数调用](chapter1/3first-instruction-in-kernel1.md#term-assembler)           |
| 链接器      | Linker                              | [为内核支持函数调用](chapter1/3first-instruction-in-kernel1.md#term-linker)              |
| 目标文件     | Object File                         | [为内核支持函数调用](chapter1/3first-instruction-in-kernel1.md#term-object-file)         |
| 链接脚本     | Linker Script                       | [为内核支持函数调用](chapter1/4first-instruction-in-kernel2.md#term-linker-script)       |
| 可执行和链接格式 | ELF, Executable and Linkable Format | [手动加载、运行应用程序](appendix-b/index.md#term-elf)                                     |
| 元数据      | Metadata                            | [手动加载、运行应用程序](appendix-b/index.md#term-metadata)                                |
| 魔数       | Magic                               | [手动加载、运行应用程序](appendix-b/index.md#term-magic)                                   |
| 裸指针      | Raw Pointer                         | [手动加载、运行应用程序](chapter1/5support-func-call.md#term-raw-pointer)                  |
| 解引用      | Dereference                         | [手动加载、运行应用程序](chapter1/5support-func-call.md#term-dereference)                  |

## 第二章：批处理系统

| 中文        | 英文                                    | 出现章节                                                            |
|-----------|---------------------------------------|-----------------------------------------------------------------|
| 批处理系统     | Batch System                          | [引言](chapter2/0intro.md#term-batch-system)                      |
| 特权级       | Privilege                             | [引言](chapter2/0intro.md#term-privilege)                         |
| 监督模式执行环境  | SEE, Supervisor Execution Environment | [RISC-V 特权级架构](chapter2/1rv-privilege.md#term-see)              |
| 异常控制流     | ECF, Exception Control Flow           | [RISC-V 特权级架构](chapter0/3os-hw-abstract.md#term-ecf)            |
| 陷入        | Trap                                  | [RISC-V 特权级架构](chapter2/1rv-privilege.md#term-trap)             |
| 异常        | Exception                             | [RISC-V 特权级架构](chapter2/1rv-privilege.md#term-exception)        |
| 执行环境调用    | Environment Call                      | [RISC-V 特权级架构](chapter2/1rv-privilege.md#term-environment-call) |
| 监督模式二进制接口 | SBI, Supervisor Binary Interface      | [RISC-V 特权级架构](chapter2/1rv-privilege.md#term-sbi)              |
| 应用程序二进制接口 | ABI, Application Binary Interface     | [RISC-V 特权级架构](chapter2/1rv-privilege.md#term-abi)              |
| 控制状态寄存器   | CSR, Control and Status Register      | [RISC-V 特权级架构](chapter2/1rv-privilege.md#term-csr)              |
| 胖指针       | Fat Pointer                           | [实现应用程序](chapter2/2application.md#term-fat-pointer)             |
| 内部可变性     | Interior Mutability                   | [实现应用程序](chapter2/3batch-system.md#term-interior-mutability)    |
| 指令缓存      | i-cache, Instruction Cache            | [实现批处理系统](chapter2/3batch-system.md#term-icache)                |
| 数据缓存      | d-cache, Data Cache                   | [实现批处理系统](chapter2/3batch-system.md#term-dcache)                |
| 原子指令      | Atomic Instruction                    | [处理 Trap](chapter8/2lock.md#term-atomic-instruction)            |

## 第三章：多道程序与分时多任务

| 中文      | 英文                        | 出现章节                                                                           |
|---------|---------------------------|--------------------------------------------------------------------------------|
| 多道程序    | Multiprogramming          | [引言](chapter3/0intro.md#term-multiprogramming)                                 |
| 分时多任务系统 | Time-Sharing Multitasking | [引言](chapter3/0intro.md#term-time-sharing-multitasking)                        |
| 任务上下文   | Task Context              | [任务切换](chapter3/2task-switching.md#term-task-context)                          |
| 输入/输出   | I/O, Input/Output         | [多道程序与协作式调度](chapter3/3multiprogramming.md#term-input-output)                  |
| 任务控制块   | Task Control Block        | [多道程序与协作式调度](chapter3/3multiprogramming.md#term-task-control-block)            |
| 吞吐量     | Throughput                | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-throughput)              |
| 后台应用    | Background Application    | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-background-application)  |
| 交互式应用   | Interactive Application   | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-interactive-application) |
| 协作式调度   | Cooperative Scheduling    | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-cooperative-scheduling)  |
| 时间片     | Time Slice                | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-time-slice)              |
| 公平性     | Fairness                  | [分时多任务系统与抢占式调度](chapter8/2lock.md#term-fairness)                               |
| 时间片轮转算法 | RR, Round-Robin           | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-round-robin)             |
| 中断      | Interrupt                 | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-interrupt)               |
| 同步      | Synchronous               | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-sync)                    |
| 异步      | Asynchronous              | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-async)                   |
| 并行      | Parallel                  | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-parallel)                |
| 软件中断    | Software Interrupt        | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-software-interrupt)      |
| 时钟中断    | Timer Interrupt           | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-timer-interrupt)         |
| 外部中断    | External Interrupt        | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-external-interrupt)      |
| 嵌套中断    | Nested Interrupt          | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-nested-interrupt)        |
| 轮询      | Busy Loop                 | [分时多任务系统与抢占式调度](chapter3/4time-sharing-system.md#term-busy-loop)               |

## 第四章：地址空间

| 中文       | 英文                                           | 出现章节                                                                                |
|----------|----------------------------------------------|-------------------------------------------------------------------------------------|
| 幻象       | Illusion                                     | [引言](chapter4/0intro.md#term-illusion)                                              |
| 时分复用     | TDM, Time-Division Multiplexing              | [引言](chapter4/0intro.md#term-time-division-multiplexing)                            |
| 地址空间     | Address Space                                | [地址空间](chapter4/2address-space.md#term-address-space)                               |
| 虚拟地址     | Virtual Address                              | [地址空间](chapter4/2address-space.md#term-virtual-address)                             |
| 内存管理单元   | MMU, Memory Management Unit                  | [地址空间](chapter4/2address-space.md#term-mmu)                                         |
| 地址转换     | Address Translation                          | [地址空间](chapter4/2address-space.md#term-address-translation)                         |
| 插槽       | Slot                                         | [地址空间](chapter4/2address-space.md#term-slot)                                        |
| 位图       | Bitmap                                       | [地址空间](chapter4/2address-space.md#term-bitmap)                                      |
| 内碎片      | Internal Fragment                            | [地址空间](chapter4/2address-space.md#term-internal-fragment)                           |
| 外碎片      | External Fragment                            | [地址空间](chapter4/2address-space.md#term-external-fragment)                           |
| 页面       | Page                                         | [地址空间](chapter4/2address-space.md#term-page)                                        |
| 虚拟页号     | VPN, Virtual Page Number                     | [地址空间](chapter4/2address-space.md#term-virtual-page-number)                         |
| 物理页号     | PPN, Physical Page Number                    | [地址空间](chapter4/2address-space.md#term-physical-page-number)                        |
| 页表       | Page Table                                   | [地址空间](chapter4/2address-space.md#term-page-table)                                  |
| 静态分配     | Static Allocation                            | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-static-allocation)        |
| 动态分配     | Dynamic Allocation                           | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-dynamic-allocation)       |
| 智能指针     | Smart Pointer                                | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-smart-pointer)            |
| 集合       | Collection                                   | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-collection)               |
| 容器       | Container                                    | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-container)                |
| 借用检查     | Borrow Check                                 | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-borrow-check)             |
| 引用计数     | Reference Counting                           | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-reference-counting)       |
| 垃圾回收     | GC, Garbage Collection                       | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-garbage-collection)       |
| 资源获取即初始化 | RAII, Resource Acquisition Is Initialization | [Rust 中的动态内存分配](chapter4/1rust-dynamic-allocation.md#term-raii)                     |
| 页内偏移     | Page Offset                                  | [实现 SV39 多级页表机制（上）](chapter4/3sv39-implementation-1.md#term-page-offset)            |
| 类型转换     | Type Conversion                              | [实现 SV39 多级页表机制（上）](chapter4/3sv39-implementation-1.md#term-type-conversion)        |
| 字典树      | Trie                                         | [实现 SV39 多级页表机制（上）](chapter4/3sv39-implementation-1.md#term-trie)                   |
| 多级页表     | Multi-Level Page Table                       | [实现 SV39 多级页表机制（上）](chapter4/3sv39-implementation-1.md#term-multi-level-page-table) |
| 页索引      | Page Index                                   | [实现 SV39 多级页表机制（上）](chapter4/3sv39-implementation-1.md#term-page-index)             |
| 大页       | Huge Page                                    | [实现 SV39 多级页表机制（上）](chapter4/3sv39-implementation-1.md#term-huge-page)              |
| 恒等映射     | Identical Mapping                            | [实现 SV39 多级页表机制（下）](chapter4/4sv39-implementation-2.md#term-identical-mapping)      |
| 页表自映射    | Recursive Mapping                            | [实现 SV39 多级页表机制（下）](chapter4/4sv39-implementation-2.md#term-recursive-mapping)      |
| 跳板       | Trampoline                                   | [内核与应用的地址空间](chapter4/6multitasking-based-on-as.md#term-trampoline)                 |
| 隔离       | Isolation                                    | [内核与应用的地址空间](chapter4/5kernel-app-spaces.md#term-isolation)                         |
| 保护页面     | Guard Page                                   | [内核与应用的地址空间](chapter4/5kernel-app-spaces.md#term-guard-page)                        |
| 快表       | Translation Lookaside Buffer                 | [基于地址空间的分时多任务](chapter4/6multitasking-based-on-as.md#term-tlb)                      |
| 熔断       | Meltdown                                     | [基于地址空间的分时多任务](chapter4/6multitasking-based-on-as.md#term-meltdown)                 |
