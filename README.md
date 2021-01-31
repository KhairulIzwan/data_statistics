# data_statistics

**Table Of Contents**


## About
A project to **automated the extraction of** **"required"** parameters from 
**original text files (.txt)** and make a copy of in **comma separated value**
**file (.csv)**.

## Installing
On Terminal, run:
```
$ git clone https://github.com/KhairulIzwan/data_statistics.git
```

## Coding Stages
1. Before finalizing and writing the codes, we were expected an output like this:
![Expected Output](https://github.com/KhairulIzwan/data_statistics/blob/main/expected.png)

2. From the original file of:
```
&&&& RUNNING TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=1 --iterations=3 --output=prob --useSpinWait
[01/12/2021-17:34:20] [I] === Model Options ===
[01/12/2021-17:34:20] [I] Format: Caffe
[01/12/2021-17:34:20] [I] Model: 
[01/12/2021-17:34:20] [I] Prototxt: Models/resnet-50.prototxt
[01/12/2021-17:34:20] [I] Output: prob
[01/12/2021-17:34:20] [I] === Build Options ===
[01/12/2021-17:34:20] [I] Max batch: 1
[01/12/2021-17:34:20] [I] Workspace: 16 MB
[01/12/2021-17:34:20] [I] minTiming: 1
[01/12/2021-17:34:20] [I] avgTiming: 8
[01/12/2021-17:34:20] [I] Precision: FP32+INT8
[01/12/2021-17:34:20] [I] Calibration: Dynamic
[01/12/2021-17:34:20] [I] Safe mode: Disabled
[01/12/2021-17:34:20] [I] Save engine: 
[01/12/2021-17:34:20] [I] Load engine: 
[01/12/2021-17:34:20] [I] Builder Cache: Enabled
[01/12/2021-17:34:20] [I] NVTX verbosity: 0
[01/12/2021-17:34:20] [I] Inputs format: fp32:CHW
[01/12/2021-17:34:20] [I] Outputs format: fp32:CHW
[01/12/2021-17:34:20] [I] Input build shapes: model
[01/12/2021-17:34:20] [I] Input calibration shapes: model
[01/12/2021-17:34:20] [I] === System Options ===
[01/12/2021-17:34:20] [I] Device: 0
[01/12/2021-17:34:20] [I] DLACore: 
[01/12/2021-17:34:20] [I] Plugins:
[01/12/2021-17:34:20] [I] === Inference Options ===
[01/12/2021-17:34:20] [I] Batch: 1
[01/12/2021-17:34:20] [I] Input inference shapes: model
[01/12/2021-17:34:20] [I] Iterations: 3
[01/12/2021-17:34:20] [I] Duration: 3s (+ 200ms warm up)
[01/12/2021-17:34:20] [I] Sleep time: 0ms
[01/12/2021-17:34:20] [I] Streams: 1
[01/12/2021-17:34:20] [I] ExposeDMA: Disabled
[01/12/2021-17:34:20] [I] Spin-wait: Enabled
[01/12/2021-17:34:20] [I] Multithreading: Disabled
[01/12/2021-17:34:20] [I] CUDA Graph: Disabled
[01/12/2021-17:34:20] [I] Skip inference: Disabled
[01/12/2021-17:34:20] [I] Inputs:
[01/12/2021-17:34:20] [I] === Reporting Options ===
[01/12/2021-17:34:20] [I] Verbose: Disabled
[01/12/2021-17:34:20] [I] Averages: 3 inferences
[01/12/2021-17:34:20] [I] Percentile: 99
[01/12/2021-17:34:20] [I] Dump output: Disabled
[01/12/2021-17:34:20] [I] Profile: Disabled
[01/12/2021-17:34:20] [I] Export timing to JSON file: 
[01/12/2021-17:34:20] [I] Export output to JSON file: 
[01/12/2021-17:34:20] [I] Export profile to JSON file: 
[01/12/2021-17:34:20] [I] 
[01/12/2021-17:34:24] [I] FP32 and INT8 precisions have been specified - more performance might be enabled by additionally specifying --fp16 or --best
[01/12/2021-17:34:24] [01/12/2021-17:34:24] [01/12/2021-17:34:33] [I] [TRT] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[01/12/2021-17:36:27] [I] [TRT] Detected 1 inputs and 1 output network tensors.
[01/12/2021-17:36:27] [I] Starting inference threads
[01/12/2021-17:36:31] [I] Warmup completed 4 queries over 200 ms
[01/12/2021-17:36:31] [I] Timing trace has 56 queries over 3.09807 s
[01/12/2021-17:36:31] [I] Trace averages of 3 runs:
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2414 ms - Host latency: 55.3046 ms (end to end 55.3169 ms, enqueue 4.07773 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.1866 ms - Host latency: 55.2487 ms (end to end 55.2664 ms, enqueue 4.05253 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2 ms - Host latency: 55.2629 ms (end to end 55.2735 ms, enqueue 4.13642 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2123 ms - Host latency: 55.2741 ms (end to end 55.2898 ms, enqueue 4.0144 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2308 ms - Host latency: 55.2938 ms (end to end 55.3122 ms, enqueue 3.99709 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2685 ms - Host latency: 55.331 ms (end to end 55.343 ms, enqueue 4.11949 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.1464 ms - Host latency: 55.2082 ms (end to end 55.2233 ms, enqueue 3.99032 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2045 ms - Host latency: 55.2667 ms (end to end 55.2799 ms, enqueue 4.03833 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2241 ms - Host latency: 55.2867 ms (end to end 55.2969 ms, enqueue 4.10942 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2379 ms - Host latency: 55.301 ms (end to end 55.308 ms, enqueue 4.02694 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.1793 ms - Host latency: 55.2412 ms (end to end 55.2539 ms, enqueue 4.07825 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.1834 ms - Host latency: 55.2458 ms (end to end 55.2581 ms, enqueue 4.12476 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.1966 ms - Host latency: 55.2591 ms (end to end 55.2699 ms, enqueue 4.15291 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.9279 ms - Host latency: 55.9919 ms (end to end 56.006 ms, enqueue 4.59147 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2103 ms - Host latency: 55.2729 ms (end to end 55.2856 ms, enqueue 4.19263 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2118 ms - Host latency: 55.2743 ms (end to end 55.2813 ms, enqueue 4.06266 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2379 ms - Host latency: 55.3005 ms (end to end 55.3146 ms, enqueue 3.96712 ms)
[01/12/2021-17:36:31] [I] Average on 3 runs - GPU latency: 55.2277 ms - Host latency: 55.291 ms (end to end 55.3049 ms, enqueue 4.15641 ms)
[01/12/2021-17:36:31] [I] Host Latency
[01/12/2021-17:36:31] [I] min: 55.1414 ms (end to end 55.1486 ms)
[01/12/2021-17:36:31] [I] max: 57.542 ms (end to end 57.561 ms)
[01/12/2021-17:36:31] [I] mean: 55.3094 ms (end to end 55.3221 ms)
[01/12/2021-17:36:31] [I] median: 55.2737 ms (end to end 55.2913 ms)
[01/12/2021-17:36:31] [I] percentile: 57.542 ms at 99% (end to end 57.561 ms at 99%)
[01/12/2021-17:36:31] [I] throughput: 18.0758 qps
[01/12/2021-17:36:31] [I] walltime: 3.09807 s
[01/12/2021-17:36:31] [I] Enqueue Time
[01/12/2021-17:36:31] [I] min: 3.87885 ms
[01/12/2021-17:36:31] [I] max: 5.10864 ms
[01/12/2021-17:36:31] [I] median: 4.06059 ms
[01/12/2021-17:36:31] [I] GPU Compute
[01/12/2021-17:36:31] [I] min: 55.0791 ms
[01/12/2021-17:36:31] [I] max: 57.4766 ms
[01/12/2021-17:36:31] [I] mean: 55.2468 ms
[01/12/2021-17:36:31] [I] median: 55.2111 ms
[01/12/2021-17:36:31] [I] percentile: 57.4766 ms at 99%
[01/12/2021-17:36:31] [I] total compute time: 3.09382 s
&&&& PASSED TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=1 --iterations=3 --output=prob --useSpinWait
&&&& RUNNING TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=4 --iterations=3 --output=prob --useSpinWait
[01/12/2021-17:36:31] [I] === Model Options ===
[01/12/2021-17:36:31] [I] Format: Caffe
[01/12/2021-17:36:31] [I] Model: 
[01/12/2021-17:36:31] [I] Prototxt: Models/resnet-50.prototxt
[01/12/2021-17:36:31] [I] Output: prob
[01/12/2021-17:36:31] [I] === Build Options ===
[01/12/2021-17:36:31] [I] Max batch: 4
[01/12/2021-17:36:31] [I] Workspace: 16 MB
[01/12/2021-17:36:31] [I] minTiming: 1
[01/12/2021-17:36:31] [I] avgTiming: 8
[01/12/2021-17:36:31] [I] Precision: FP32+INT8
[01/12/2021-17:36:31] [I] Calibration: Dynamic
[01/12/2021-17:36:31] [I] Safe mode: Disabled
[01/12/2021-17:36:31] [I] Save engine: 
[01/12/2021-17:36:31] [I] Load engine: 
[01/12/2021-17:36:31] [I] Builder Cache: Enabled
[01/12/2021-17:36:31] [I] NVTX verbosity: 0
[01/12/2021-17:36:31] [I] Inputs format: fp32:CHW
[01/12/2021-17:36:31] [I] Outputs format: fp32:CHW
[01/12/2021-17:36:31] [I] Input build shapes: model
[01/12/2021-17:36:31] [I] Input calibration shapes: model
[01/12/2021-17:36:31] [I] === System Options ===
[01/12/2021-17:36:31] [I] Device: 0
[01/12/2021-17:36:31] [I] DLACore: 
[01/12/2021-17:36:31] [I] Plugins:
[01/12/2021-17:36:31] [I] === Inference Options ===
[01/12/2021-17:36:31] [I] Batch: 4
[01/12/2021-17:36:31] [I] Input inference shapes: model
[01/12/2021-17:36:31] [I] Iterations: 3
[01/12/2021-17:36:31] [I] Duration: 3s (+ 200ms warm up)
[01/12/2021-17:36:31] [I] Sleep time: 0ms
[01/12/2021-17:36:31] [I] Streams: 1
[01/12/2021-17:36:31] [I] ExposeDMA: Disabled
[01/12/2021-17:36:31] [I] Spin-wait: Enabled
[01/12/2021-17:36:31] [I] Multithreading: Disabled
[01/12/2021-17:36:31] [I] CUDA Graph: Disabled
[01/12/2021-17:36:31] [I] Skip inference: Disabled
[01/12/2021-17:36:31] [I] Inputs:
[01/12/2021-17:36:31] [I] === Reporting Options ===
[01/12/2021-17:36:31] [I] Verbose: Disabled
[01/12/2021-17:36:31] [I] Averages: 3 inferences
[01/12/2021-17:36:31] [I] Percentile: 99
[01/12/2021-17:36:31] [I] Dump output: Disabled
[01/12/2021-17:36:31] [I] Profile: Disabled
[01/12/2021-17:36:31] [I] Export timing to JSON file: 
[01/12/2021-17:36:31] [I] Export output to JSON file: 
[01/12/2021-17:36:31] [I] Export profile to JSON file: 
[01/12/2021-17:36:31] [I] 
[01/12/2021-17:36:35] [I] FP32 and INT8 precisions have been specified - more performance might be enabled by additionally specifying --fp16 or --best
[01/12/2021-17:36:35] [01/12/2021-17:36:35] [01/12/2021-17:36:42] [I] [TRT] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[01/12/2021-17:37:09] [I] [TRT] Detected 1 inputs and 1 output network tensors.
[01/12/2021-17:37:09] [I] Starting inference threads
[01/12/2021-17:37:13] [I] Warmup completed 4 queries over 200 ms
[01/12/2021-17:37:13] [I] Timing trace has 68 queries over 3.39842 s
[01/12/2021-17:37:13] [I] Trace averages of 3 runs:
[01/12/2021-17:37:13] [I] Average on 3 runs - GPU latency: 199.357 ms - Host latency: 199.608 ms (end to end 199.615 ms, enqueue 5.11208 ms)
[01/12/2021-17:37:13] [I] Average on 3 runs - GPU latency: 199.698 ms - Host latency: 199.951 ms (end to end 199.956 ms, enqueue 5.18567 ms)
[01/12/2021-17:37:13] [I] Average on 3 runs - GPU latency: 199.568 ms - Host latency: 199.82 ms (end to end 199.825 ms, enqueue 5.24939 ms)
[01/12/2021-17:37:13] [I] Average on 3 runs - GPU latency: 200.234 ms - Host latency: 200.486 ms (end to end 200.492 ms, enqueue 5.15377 ms)
[01/12/2021-17:37:13] [I] Average on 3 runs - GPU latency: 199.474 ms - Host latency: 199.728 ms (end to end 199.734 ms, enqueue 5.45817 ms)
[01/12/2021-17:37:13] [I] Host Latency
[01/12/2021-17:37:13] [I] min: 199.272 ms (end to end 199.278 ms)
[01/12/2021-17:37:13] [I] max: 202.241 ms (end to end 202.247 ms)
[01/12/2021-17:37:13] [I] mean: 199.901 ms (end to end 199.907 ms)
[01/12/2021-17:37:13] [I] median: 199.829 ms (end to end 199.835 ms)
[01/12/2021-17:37:13] [I] percentile: 202.241 ms at 99% (end to end 202.247 ms at 99%)
[01/12/2021-17:37:13] [I] throughput: 20.0093 qps
[01/12/2021-17:37:13] [I] walltime: 3.39842 s
[01/12/2021-17:37:13] [I] Enqueue Time
[01/12/2021-17:37:13] [I] min: 4.84339 ms
[01/12/2021-17:37:13] [I] max: 5.58545 ms
[01/12/2021-17:37:13] [I] median: 5.20312 ms
[01/12/2021-17:37:13] [I] GPU Compute
[01/12/2021-17:37:13] [I] min: 199.02 ms
[01/12/2021-17:37:13] [I] max: 201.991 ms
[01/12/2021-17:37:13] [I] mean: 199.649 ms
[01/12/2021-17:37:13] [I] median: 199.573 ms
[01/12/2021-17:37:13] [I] percentile: 201.991 ms at 99%
[01/12/2021-17:37:13] [I] total compute time: 3.39403 s
&&&& PASSED TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=4 --iterations=3 --output=prob --useSpinWait
&&&& RUNNING TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=8 --iterations=3 --output=prob --useSpinWait
[01/12/2021-17:37:13] [I] === Model Options ===
[01/12/2021-17:37:13] [I] Format: Caffe
[01/12/2021-17:37:13] [I] Model: 
[01/12/2021-17:37:13] [I] Prototxt: Models/resnet-50.prototxt
[01/12/2021-17:37:13] [I] Output: prob
[01/12/2021-17:37:13] [I] === Build Options ===
[01/12/2021-17:37:13] [I] Max batch: 8
[01/12/2021-17:37:13] [I] Workspace: 16 MB
[01/12/2021-17:37:13] [I] minTiming: 1
[01/12/2021-17:37:13] [I] avgTiming: 8
[01/12/2021-17:37:13] [I] Precision: FP32+INT8
[01/12/2021-17:37:13] [I] Calibration: Dynamic
[01/12/2021-17:37:13] [I] Safe mode: Disabled
[01/12/2021-17:37:13] [I] Save engine: 
[01/12/2021-17:37:13] [I] Load engine: 
[01/12/2021-17:37:13] [I] Builder Cache: Enabled
[01/12/2021-17:37:13] [I] NVTX verbosity: 0
[01/12/2021-17:37:13] [I] Inputs format: fp32:CHW
[01/12/2021-17:37:13] [I] Outputs format: fp32:CHW
[01/12/2021-17:37:13] [I] Input build shapes: model
[01/12/2021-17:37:13] [I] Input calibration shapes: model
[01/12/2021-17:37:13] [I] === System Options ===
[01/12/2021-17:37:13] [I] Device: 0
[01/12/2021-17:37:13] [I] DLACore: 
[01/12/2021-17:37:13] [I] Plugins:
[01/12/2021-17:37:13] [I] === Inference Options ===
[01/12/2021-17:37:13] [I] Batch: 8
[01/12/2021-17:37:13] [I] Input inference shapes: model
[01/12/2021-17:37:13] [I] Iterations: 3
[01/12/2021-17:37:13] [I] Duration: 3s (+ 200ms warm up)
[01/12/2021-17:37:13] [I] Sleep time: 0ms
[01/12/2021-17:37:13] [I] Streams: 1
[01/12/2021-17:37:13] [I] ExposeDMA: Disabled
[01/12/2021-17:37:13] [I] Spin-wait: Enabled
[01/12/2021-17:37:13] [I] Multithreading: Disabled
[01/12/2021-17:37:13] [I] CUDA Graph: Disabled
[01/12/2021-17:37:13] [I] Skip inference: Disabled
[01/12/2021-17:37:13] [I] Inputs:
[01/12/2021-17:37:13] [I] === Reporting Options ===
[01/12/2021-17:37:13] [I] Verbose: Disabled
[01/12/2021-17:37:13] [I] Averages: 3 inferences
[01/12/2021-17:37:13] [I] Percentile: 99
[01/12/2021-17:37:13] [I] Dump output: Disabled
[01/12/2021-17:37:13] [I] Profile: Disabled
[01/12/2021-17:37:13] [I] Export timing to JSON file: 
[01/12/2021-17:37:13] [I] Export output to JSON file: 
[01/12/2021-17:37:13] [I] Export profile to JSON file: 
[01/12/2021-17:37:13] [I] 
[01/12/2021-17:37:17] [I] FP32 and INT8 precisions have been specified - more performance might be enabled by additionally specifying --fp16 or --best
[01/12/2021-17:37:17] [01/12/2021-17:37:17] [01/12/2021-17:37:26] [I] [TRT] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[01/12/2021-17:38:10] [I] [TRT] Detected 1 inputs and 1 output network tensors.
[01/12/2021-17:38:11] [I] Starting inference threads
[01/12/2021-17:38:15] [I] Warmup completed 8 queries over 200 ms
[01/12/2021-17:38:15] [I] Timing trace has 80 queries over 3.74516 s
[01/12/2021-17:38:15] [I] Trace averages of 3 runs:
[01/12/2021-17:38:15] [I] Average on 3 runs - GPU latency: 373.409 ms - Host latency: 373.916 ms (end to end 373.922 ms, enqueue 4.93357 ms)
[01/12/2021-17:38:15] [I] Average on 3 runs - GPU latency: 374.967 ms - Host latency: 375.476 ms (end to end 375.482 ms, enqueue 5.15308 ms)
[01/12/2021-17:38:15] [I] Average on 3 runs - GPU latency: 373.734 ms - Host latency: 374.239 ms (end to end 374.245 ms, enqueue 5.21598 ms)
[01/12/2021-17:38:15] [I] Host Latency
[01/12/2021-17:38:15] [I] min: 373.747 ms (end to end 373.753 ms)
[01/12/2021-17:38:15] [I] max: 377.474 ms (end to end 377.48 ms)
[01/12/2021-17:38:15] [I] mean: 374.51 ms (end to end 374.515 ms)
[01/12/2021-17:38:15] [I] median: 374.178 ms (end to end 374.183 ms)
[01/12/2021-17:38:15] [I] percentile: 377.474 ms at 99% (end to end 377.48 ms at 99%)
[01/12/2021-17:38:15] [I] throughput: 21.3609 qps
[01/12/2021-17:38:15] [I] walltime: 3.74516 s
[01/12/2021-17:38:15] [I] Enqueue Time
[01/12/2021-17:38:15] [I] min: 4.68089 ms
[01/12/2021-17:38:15] [I] max: 5.27795 ms
[01/12/2021-17:38:15] [I] median: 5.10193 ms
[01/12/2021-17:38:15] [I] GPU Compute
[01/12/2021-17:38:15] [I] min: 373.242 ms
[01/12/2021-17:38:15] [I] max: 376.966 ms
[01/12/2021-17:38:15] [I] mean: 374.004 ms
[01/12/2021-17:38:15] [I] median: 373.68 ms
[01/12/2021-17:38:15] [I] percentile: 376.966 ms at 99%
[01/12/2021-17:38:15] [I] total compute time: 3.74004 s
&&&& PASSED TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=8 --iterations=3 --output=prob --useSpinWait
&&&& RUNNING TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=16 --iterations=3 --output=prob --useSpinWait
[01/12/2021-17:38:16] [I] === Model Options ===
[01/12/2021-17:38:16] [I] Format: Caffe
[01/12/2021-17:38:16] [I] Model: 
[01/12/2021-17:38:16] [I] Prototxt: Models/resnet-50.prototxt
[01/12/2021-17:38:16] [I] Output: prob
[01/12/2021-17:38:16] [I] === Build Options ===
[01/12/2021-17:38:16] [I] Max batch: 16
[01/12/2021-17:38:16] [I] Workspace: 16 MB
[01/12/2021-17:38:16] [I] minTiming: 1
[01/12/2021-17:38:16] [I] avgTiming: 8
[01/12/2021-17:38:16] [I] Precision: FP32+INT8
[01/12/2021-17:38:16] [I] Calibration: Dynamic
[01/12/2021-17:38:16] [I] Safe mode: Disabled
[01/12/2021-17:38:16] [I] Save engine: 
[01/12/2021-17:38:16] [I] Load engine: 
[01/12/2021-17:38:16] [I] Builder Cache: Enabled
[01/12/2021-17:38:16] [I] NVTX verbosity: 0
[01/12/2021-17:38:16] [I] Inputs format: fp32:CHW
[01/12/2021-17:38:16] [I] Outputs format: fp32:CHW
[01/12/2021-17:38:16] [I] Input build shapes: model
[01/12/2021-17:38:16] [I] Input calibration shapes: model
[01/12/2021-17:38:16] [I] === System Options ===
[01/12/2021-17:38:16] [I] Device: 0
[01/12/2021-17:38:16] [I] DLACore: 
[01/12/2021-17:38:16] [I] Plugins:
[01/12/2021-17:38:16] [I] === Inference Options ===
[01/12/2021-17:38:16] [I] Batch: 16
[01/12/2021-17:38:16] [I] Input inference shapes: model
[01/12/2021-17:38:16] [I] Iterations: 3
[01/12/2021-17:38:16] [I] Duration: 3s (+ 200ms warm up)
[01/12/2021-17:38:16] [I] Sleep time: 0ms
[01/12/2021-17:38:16] [I] Streams: 1
[01/12/2021-17:38:16] [I] ExposeDMA: Disabled
[01/12/2021-17:38:16] [I] Spin-wait: Enabled
[01/12/2021-17:38:16] [I] Multithreading: Disabled
[01/12/2021-17:38:16] [I] CUDA Graph: Disabled
[01/12/2021-17:38:16] [I] Skip inference: Disabled
[01/12/2021-17:38:16] [I] Inputs:
[01/12/2021-17:38:16] [I] === Reporting Options ===
[01/12/2021-17:38:16] [I] Verbose: Disabled
[01/12/2021-17:38:16] [I] Averages: 3 inferences
[01/12/2021-17:38:16] [I] Percentile: 99
[01/12/2021-17:38:16] [I] Dump output: Disabled
[01/12/2021-17:38:16] [I] Profile: Disabled
[01/12/2021-17:38:16] [I] Export timing to JSON file: 
[01/12/2021-17:38:16] [I] Export output to JSON file: 
[01/12/2021-17:38:16] [I] Export profile to JSON file: 
[01/12/2021-17:38:16] [I] 
[01/12/2021-17:38:19] [I] FP32 and INT8 precisions have been specified - more performance might be enabled by additionally specifying --fp16 or --best
[01/12/2021-17:38:19] [01/12/2021-17:38:19] [01/12/2021-17:38:31] [I] [TRT] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[01/12/2021-17:39:52] [I] [TRT] Detected 1 inputs and 1 output network tensors.
[01/12/2021-17:39:53] [I] Starting inference threads
[01/12/2021-17:39:58] [I] Warmup completed 16 queries over 200 ms
[01/12/2021-17:39:58] [I] Timing trace has 96 queries over 4.29733 s
[01/12/2021-17:39:58] [I] Trace averages of 3 runs:
[01/12/2021-17:39:58] [I] Average on 3 runs - GPU latency: 715.607 ms - Host latency: 716.612 ms (end to end 716.618 ms, enqueue 5.19342 ms)
[01/12/2021-17:39:58] [I] Average on 3 runs - GPU latency: 714.823 ms - Host latency: 715.819 ms (end to end 715.824 ms, enqueue 5.39697 ms)
[01/12/2021-17:39:58] [I] Host Latency
[01/12/2021-17:39:58] [I] min: 714.088 ms (end to end 714.092 ms)
[01/12/2021-17:39:58] [I] max: 718.343 ms (end to end 718.349 ms)
[01/12/2021-17:39:58] [I] mean: 716.216 ms (end to end 716.221 ms)
[01/12/2021-17:39:58] [I] median: 716.657 ms (end to end 716.663 ms)
[01/12/2021-17:39:58] [I] percentile: 718.343 ms at 99% (end to end 718.349 ms at 99%)
[01/12/2021-17:39:58] [I] throughput: 22.3395 qps
[01/12/2021-17:39:58] [I] walltime: 4.29733 s
[01/12/2021-17:39:58] [I] Enqueue Time
[01/12/2021-17:39:58] [I] min: 4.80229 ms
[01/12/2021-17:39:58] [I] max: 5.45044 ms
[01/12/2021-17:39:58] [I] median: 5.37592 ms
[01/12/2021-17:39:58] [I] GPU Compute
[01/12/2021-17:39:58] [I] min: 713.122 ms
[01/12/2021-17:39:58] [I] max: 717.336 ms
[01/12/2021-17:39:58] [I] mean: 715.215 ms
[01/12/2021-17:39:58] [I] median: 715.649 ms
[01/12/2021-17:39:58] [I] percentile: 717.336 ms at 99%
[01/12/2021-17:39:58] [I] total compute time: 4.29129 s
&&&& PASSED TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=16 --iterations=3 --output=prob --useSpinWait
&&&& RUNNING TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=32 --iterations=3 --output=prob --useSpinWait
[01/12/2021-17:39:59] [I] === Model Options ===
[01/12/2021-17:39:59] [I] Format: Caffe
[01/12/2021-17:39:59] [I] Model: 
[01/12/2021-17:39:59] [I] Prototxt: Models/resnet-50.prototxt
[01/12/2021-17:39:59] [I] Output: prob
[01/12/2021-17:39:59] [I] === Build Options ===
[01/12/2021-17:39:59] [I] Max batch: 32
[01/12/2021-17:39:59] [I] Workspace: 16 MB
[01/12/2021-17:39:59] [I] minTiming: 1
[01/12/2021-17:39:59] [I] avgTiming: 8
[01/12/2021-17:39:59] [I] Precision: FP32+INT8
[01/12/2021-17:39:59] [I] Calibration: Dynamic
[01/12/2021-17:39:59] [I] Safe mode: Disabled
[01/12/2021-17:39:59] [I] Save engine: 
[01/12/2021-17:39:59] [I] Load engine: 
[01/12/2021-17:39:59] [I] Builder Cache: Enabled
[01/12/2021-17:39:59] [I] NVTX verbosity: 0
[01/12/2021-17:39:59] [I] Inputs format: fp32:CHW
[01/12/2021-17:39:59] [I] Outputs format: fp32:CHW
[01/12/2021-17:39:59] [I] Input build shapes: model
[01/12/2021-17:39:59] [I] Input calibration shapes: model
[01/12/2021-17:39:59] [I] === System Options ===
[01/12/2021-17:39:59] [I] Device: 0
[01/12/2021-17:39:59] [I] DLACore: 
[01/12/2021-17:39:59] [I] Plugins:
[01/12/2021-17:39:59] [I] === Inference Options ===
[01/12/2021-17:39:59] [I] Batch: 32
[01/12/2021-17:39:59] [I] Input inference shapes: model
[01/12/2021-17:39:59] [I] Iterations: 3
[01/12/2021-17:39:59] [I] Duration: 3s (+ 200ms warm up)
[01/12/2021-17:39:59] [I] Sleep time: 0ms
[01/12/2021-17:39:59] [I] Streams: 1
[01/12/2021-17:39:59] [I] ExposeDMA: Disabled
[01/12/2021-17:39:59] [I] Spin-wait: Enabled
[01/12/2021-17:39:59] [I] Multithreading: Disabled
[01/12/2021-17:39:59] [I] CUDA Graph: Disabled
[01/12/2021-17:39:59] [I] Skip inference: Disabled
[01/12/2021-17:39:59] [I] Inputs:
[01/12/2021-17:39:59] [I] === Reporting Options ===
[01/12/2021-17:39:59] [I] Verbose: Disabled
[01/12/2021-17:39:59] [I] Averages: 3 inferences
[01/12/2021-17:39:59] [I] Percentile: 99
[01/12/2021-17:39:59] [I] Dump output: Disabled
[01/12/2021-17:39:59] [I] Profile: Disabled
[01/12/2021-17:39:59] [I] Export timing to JSON file: 
[01/12/2021-17:39:59] [I] Export output to JSON file: 
[01/12/2021-17:39:59] [I] Export profile to JSON file: 
[01/12/2021-17:39:59] [I] 
[01/12/2021-17:40:02] [I] FP32 and INT8 precisions have been specified - more performance might be enabled by additionally specifying --fp16 or --best
[01/12/2021-17:40:02] [01/12/2021-17:40:02] [01/12/2021-17:40:17] [I] [TRT] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[01/12/2021-17:42:46] [I] [TRT] Detected 1 inputs and 1 output network tensors.
[01/12/2021-17:42:47] [I] Starting inference threads
[01/12/2021-17:42:54] [I] Warmup completed 32 queries over 200 ms
[01/12/2021-17:42:54] [I] Timing trace has 128 queries over 5.45773 s
[01/12/2021-17:42:54] [I] Trace averages of 3 runs:
[01/12/2021-17:42:54] [I] Average on 3 runs - GPU latency: 1362.61 ms - Host latency: 1364.65 ms (end to end 1364.65 ms, enqueue 5.7388 ms)
[01/12/2021-17:42:54] [I] Host Latency
[01/12/2021-17:42:54] [I] min: 1362.14 ms (end to end 1362.15 ms)
[01/12/2021-17:42:54] [I] max: 1366.84 ms (end to end 1366.85 ms)
[01/12/2021-17:42:54] [I] mean: 1364.43 ms (end to end 1364.43 ms)
[01/12/2021-17:42:54] [I] median: 1364.36 ms (end to end 1364.36 ms)
[01/12/2021-17:42:54] [I] percentile: 1366.84 ms at 99% (end to end 1366.85 ms at 99%)
[01/12/2021-17:42:54] [I] throughput: 23.453 qps
[01/12/2021-17:42:54] [I] walltime: 5.45773 s
[01/12/2021-17:42:54] [I] Enqueue Time
[01/12/2021-17:42:54] [I] min: 5.21604 ms
[01/12/2021-17:42:54] [I] max: 6.06812 ms
[01/12/2021-17:42:54] [I] median: 5.90363 ms
[01/12/2021-17:42:54] [I] GPU Compute
[01/12/2021-17:42:54] [I] min: 1360.1 ms
[01/12/2021-17:42:54] [I] max: 1364.81 ms
[01/12/2021-17:42:54] [I] mean: 1362.41 ms
[01/12/2021-17:42:54] [I] median: 1362.37 ms
[01/12/2021-17:42:54] [I] percentile: 1364.81 ms at 99%
[01/12/2021-17:42:54] [I] total compute time: 5.44965 s
&&&& PASSED TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=32 --iterations=3 --output=prob --useSpinWait
&&&& RUNNING TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=64 --iterations=3 --output=prob --useSpinWait
[01/12/2021-17:42:55] [I] === Model Options ===
[01/12/2021-17:42:55] [I] Format: Caffe
[01/12/2021-17:42:55] [I] Model: 
[01/12/2021-17:42:55] [I] Prototxt: Models/resnet-50.prototxt
[01/12/2021-17:42:55] [I] Output: prob
[01/12/2021-17:42:55] [I] === Build Options ===
[01/12/2021-17:42:55] [I] Max batch: 64
[01/12/2021-17:42:55] [I] Workspace: 16 MB
[01/12/2021-17:42:55] [I] minTiming: 1
[01/12/2021-17:42:55] [I] avgTiming: 8
[01/12/2021-17:42:55] [I] Precision: FP32+INT8
[01/12/2021-17:42:55] [I] Calibration: Dynamic
[01/12/2021-17:42:55] [I] Safe mode: Disabled
[01/12/2021-17:42:55] [I] Save engine: 
[01/12/2021-17:42:55] [I] Load engine: 
[01/12/2021-17:42:55] [I] Builder Cache: Enabled
[01/12/2021-17:42:55] [I] NVTX verbosity: 0
[01/12/2021-17:42:55] [I] Inputs format: fp32:CHW
[01/12/2021-17:42:55] [I] Outputs format: fp32:CHW
[01/12/2021-17:42:55] [I] Input build shapes: model
[01/12/2021-17:42:55] [I] Input calibration shapes: model
[01/12/2021-17:42:55] [I] === System Options ===
[01/12/2021-17:42:55] [I] Device: 0
[01/12/2021-17:42:55] [I] DLACore: 
[01/12/2021-17:42:55] [I] Plugins:
[01/12/2021-17:42:55] [I] === Inference Options ===
[01/12/2021-17:42:55] [I] Batch: 64
[01/12/2021-17:42:55] [I] Input inference shapes: model
[01/12/2021-17:42:55] [I] Iterations: 3
[01/12/2021-17:42:55] [I] Duration: 3s (+ 200ms warm up)
[01/12/2021-17:42:55] [I] Sleep time: 0ms
[01/12/2021-17:42:55] [I] Streams: 1
[01/12/2021-17:42:55] [I] ExposeDMA: Disabled
[01/12/2021-17:42:55] [I] Spin-wait: Enabled
[01/12/2021-17:42:55] [I] Multithreading: Disabled
[01/12/2021-17:42:55] [I] CUDA Graph: Disabled
[01/12/2021-17:42:55] [I] Skip inference: Disabled
[01/12/2021-17:42:55] [I] Inputs:
[01/12/2021-17:42:55] [I] === Reporting Options ===
[01/12/2021-17:42:55] [I] Verbose: Disabled
[01/12/2021-17:42:55] [I] Averages: 3 inferences
[01/12/2021-17:42:55] [I] Percentile: 99
[01/12/2021-17:42:55] [I] Dump output: Disabled
[01/12/2021-17:42:55] [I] Profile: Disabled
[01/12/2021-17:42:55] [I] Export timing to JSON file: 
[01/12/2021-17:42:55] [I] Export output to JSON file: 
[01/12/2021-17:42:55] [I] Export profile to JSON file: 
[01/12/2021-17:42:55] [I] 
[01/12/2021-17:42:58] [I] FP32 and INT8 precisions have been specified - more performance might be enabled by additionally specifying --fp16 or --best
[01/12/2021-17:42:58] [01/12/2021-17:42:58] [01/12/2021-17:43:24] [I] [TRT] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[01/12/2021-17:48:11] [I] [TRT] Detected 1 inputs and 1 output network tensors.
[01/12/2021-17:48:13] [I] Starting inference threads
[01/12/2021-17:48:24] [I] Warmup completed 64 queries over 200 ms
[01/12/2021-17:48:24] [I] Timing trace has 192 queries over 7.76538 s
[01/12/2021-17:48:24] [I] Trace averages of 3 runs:
[01/12/2021-17:48:24] [I] Average on 3 runs - GPU latency: 2584.38 ms - Host latency: 2588.45 ms (end to end 2588.46 ms, enqueue 6.80625 ms)
[01/12/2021-17:48:24] [I] Host Latency
[01/12/2021-17:48:24] [I] min: 2581.83 ms (end to end 2581.84 ms)
[01/12/2021-17:48:24] [I] max: 2591.81 ms (end to end 2591.82 ms)
[01/12/2021-17:48:24] [I] mean: 2588.45 ms (end to end 2588.46 ms)
[01/12/2021-17:48:24] [I] median: 2591.72 ms (end to end 2591.72 ms)
[01/12/2021-17:48:24] [I] percentile: 2591.81 ms at 99% (end to end 2591.82 ms at 99%)
[01/12/2021-17:48:24] [I] throughput: 24.7251 qps
[01/12/2021-17:48:24] [I] walltime: 7.76538 s
[01/12/2021-17:48:24] [I] Enqueue Time
[01/12/2021-17:48:24] [I] min: 6.3667 ms
[01/12/2021-17:48:24] [I] max: 7.4837 ms
[01/12/2021-17:48:24] [I] median: 6.56836 ms
[01/12/2021-17:48:24] [I] GPU Compute
[01/12/2021-17:48:24] [I] min: 2577.87 ms
[01/12/2021-17:48:24] [I] max: 2587.68 ms
[01/12/2021-17:48:24] [I] mean: 2584.38 ms
[01/12/2021-17:48:24] [I] median: 2587.59 ms
[01/12/2021-17:48:24] [I] percentile: 2587.68 ms at 99%
[01/12/2021-17:48:24] [I] total compute time: 7.75314 s
&&&& PASSED TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=64 --iterations=3 --output=prob --useSpinWait
&&&& RUNNING TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=128 --iterations=3 --output=prob --useSpinWait
[01/12/2021-17:48:24] [I] === Model Options ===
[01/12/2021-17:48:24] [I] Format: Caffe
[01/12/2021-17:48:24] [I] Model: 
[01/12/2021-17:48:24] [I] Prototxt: Models/resnet-50.prototxt
[01/12/2021-17:48:24] [I] Output: prob
[01/12/2021-17:48:24] [I] === Build Options ===
[01/12/2021-17:48:24] [I] Max batch: 128
[01/12/2021-17:48:24] [I] Workspace: 16 MB
[01/12/2021-17:48:24] [I] minTiming: 1
[01/12/2021-17:48:24] [I] avgTiming: 8
[01/12/2021-17:48:24] [I] Precision: FP32+INT8
[01/12/2021-17:48:24] [I] Calibration: Dynamic
[01/12/2021-17:48:24] [I] Safe mode: Disabled
[01/12/2021-17:48:24] [I] Save engine: 
[01/12/2021-17:48:24] [I] Load engine: 
[01/12/2021-17:48:24] [I] Builder Cache: Enabled
[01/12/2021-17:48:24] [I] NVTX verbosity: 0
[01/12/2021-17:48:24] [I] Inputs format: fp32:CHW
[01/12/2021-17:48:24] [I] Outputs format: fp32:CHW
[01/12/2021-17:48:24] [I] Input build shapes: model
[01/12/2021-17:48:24] [I] Input calibration shapes: model
[01/12/2021-17:48:24] [I] === System Options ===
[01/12/2021-17:48:24] [I] Device: 0
[01/12/2021-17:48:24] [I] DLACore: 
[01/12/2021-17:48:24] [I] Plugins:
[01/12/2021-17:48:24] [I] === Inference Options ===
[01/12/2021-17:48:24] [I] Batch: 128
[01/12/2021-17:48:24] [I] Input inference shapes: model
[01/12/2021-17:48:24] [I] Iterations: 3
[01/12/2021-17:48:24] [I] Duration: 3s (+ 200ms warm up)
[01/12/2021-17:48:24] [I] Sleep time: 0ms
[01/12/2021-17:48:24] [I] Streams: 1
[01/12/2021-17:48:24] [I] ExposeDMA: Disabled
[01/12/2021-17:48:24] [I] Spin-wait: Enabled
[01/12/2021-17:48:24] [I] Multithreading: Disabled
[01/12/2021-17:48:24] [I] CUDA Graph: Disabled
[01/12/2021-17:48:24] [I] Skip inference: Disabled
[01/12/2021-17:48:24] [I] Inputs:
[01/12/2021-17:48:24] [I] === Reporting Options ===
[01/12/2021-17:48:24] [I] Verbose: Disabled
[01/12/2021-17:48:24] [I] Averages: 3 inferences
[01/12/2021-17:48:24] [I] Percentile: 99
[01/12/2021-17:48:24] [I] Dump output: Disabled
[01/12/2021-17:48:24] [I] Profile: Disabled
[01/12/2021-17:48:24] [I] Export timing to JSON file: 
[01/12/2021-17:48:24] [I] Export output to JSON file: 
[01/12/2021-17:48:24] [I] Export profile to JSON file: 
[01/12/2021-17:48:24] [I] 
[01/12/2021-17:48:28] [I] FP32 and INT8 precisions have been specified - more performance might be enabled by additionally specifying --fp16 or --best
[01/12/2021-17:48:28] [01/12/2021-17:48:28] [01/12/2021-17:49:17] [I] [TRT] Some tactics do not have sufficient workspace memory to run. Increasing workspace size may increase performance, please check verbose output.
[01/12/2021-17:58:41] [I] [TRT] Detected 1 inputs and 1 output network tensors.
[01/12/2021-17:58:45] [I] Starting inference threads
[01/12/2021-17:59:06] [I] Warmup completed 128 queries over 200 ms
[01/12/2021-17:59:06] [I] Timing trace has 384 queries over 15.4969 s
[01/12/2021-17:59:06] [I] Trace averages of 3 runs:
[01/12/2021-17:59:06] [I] Average on 3 runs - GPU latency: 5157.54 ms - Host latency: 5165.61 ms (end to end 5165.62 ms, enqueue 6.35434 ms)
[01/12/2021-17:59:06] [I] Host Latency
[01/12/2021-17:59:06] [I] min: 5159.68 ms (end to end 5159.68 ms)
[01/12/2021-17:59:06] [I] max: 5173.78 ms (end to end 5173.79 ms)
[01/12/2021-17:59:06] [I] mean: 5165.61 ms (end to end 5165.62 ms)
[01/12/2021-17:59:06] [I] median: 5163.39 ms (end to end 5163.39 ms)
[01/12/2021-17:59:06] [I] percentile: 5173.78 ms at 99% (end to end 5173.79 ms at 99%)
[01/12/2021-17:59:06] [I] throughput: 24.7792 qps
[01/12/2021-17:59:06] [I] walltime: 15.4969 s
[01/12/2021-17:59:06] [I] Enqueue Time
[01/12/2021-17:59:06] [I] min: 5.6475 ms
[01/12/2021-17:59:06] [I] max: 6.70947 ms
[01/12/2021-17:59:06] [I] median: 6.70605 ms
[01/12/2021-17:59:06] [I] GPU Compute
[01/12/2021-17:59:06] [I] min: 5151.77 ms
[01/12/2021-17:59:06] [I] max: 5165.62 ms
[01/12/2021-17:59:06] [I] mean: 5157.54 ms
[01/12/2021-17:59:06] [I] median: 5155.22 ms
[01/12/2021-17:59:06] [I] percentile: 5165.62 ms at 99%
[01/12/2021-17:59:06] [I] total compute time: 15.4726 s
&&&& PASSED TensorRT.trtexec # /usr/src/tensorrt/bin/trtexec --avgRuns=3 --deploy=Models/resnet-50.prototxt --int8 --batch=128 --iterations=3 --output=prob --useSpinWait
```
3. So, we known that all required "parameter" on the expected output are:
	1. 'Format:'
	2. 'Prototxt:'
	3. 'Precision:'
	4. 'Iterations:'
	5. 'Batch:'
	6. 'throughput:'
	
which were located under various "header" listed below:
	1. "=== Model Options ===", 
	2. "=== Build Options ===", 
	3. "=== Inference Options ===", 
	4. "=== Reporting Options ==="

## Usage
#### Hardcoded
1. On terminal, run:
```
python extract_hardcoded.py
```
#### Flawless
1. On terminal, run:
```
python extract_trtexec.py
```

## Ouput
[Result](https://github.com/KhairulIzwan/data_statistics/blob/main/files/GPU-int8_resnet-50-January%2018%2C%202021%2008:30:14.csv)

## References:
1. [Python Read Text File](https://www.pythontutorial.net/python-basics/python-read-text-file/)
2. [Count number of lines in a text file in Python](https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/)
3. [Python: Search strings in a file and get line numbers of lines containing the string](https://thispointer.com/python-search-strings-in-a-file-and-get-line-numbers-of-lines-containing-the-string/)
4. [Check if all elements in a list are identical](https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical)
5. [Printing boolean values True/False with the format() method in Python](https://stackoverflow.com/questions/23655005/printing-boolean-values-true-false-with-the-format-method-in-python)
6. [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/#writing-csv-files-with-csv)
7. [Python exit commands: quit(), exit(), sys.exit() and os._exit()](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/)
8. [Python Program to Print Pattern – Print Number, Star, Pyramid, Diamond and Letter Pattern](https://pynative.com/print-pattern-python-examples/)
9. [https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/](https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/)
10. [https://www.w3resource.com/python-exercises/python-basic-exercise-99.php](https://www.w3resource.com/python-exercises/python-basic-exercise-99.php)
11. [How to get current date and time in Python?](https://www.programiz.com/python-programming/datetime/current-datetime)
