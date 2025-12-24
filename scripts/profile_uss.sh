#!/usr/bin/env bash
#
# profile_uss.sh
#
# Copyright (C) 2025 Lambda Research Collective
#
# This file is part of Lambda Calculus Research Repository.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


# Unified Spandrel Synthesis - Profiling Script
# Targets SM89 / CUDA 12

LOG_FILE="logs/profiling_$(date +%Y%m%d_%H%M%S).log"

echo "Starting USS Experimental Pipeline Profiling..." | tee -a $LOG_FILE

# 1. Hardware Audit
echo "--- Hardware Audit ---" | tee -a $LOG_FILE
nvidia-smi --query-gpu=name,compute_cap,memory.total --format=csv | tee -a $LOG_FILE

# 2. Baseline Performance (CPU/GPU Fallback)
echo "--- Baseline Execution ---" | tee -a $LOG_FILE
python3 src/experiments/uss_pipeline.py 2>&1 | tee -a $LOG_FILE

# 3. Kernel Profiling (if nvprof is available)
if command -v nvprof &> /dev/null
then
    echo "--- CUDA Kernel Profiling (nvprof) ---" | tee -a $LOG_FILE
    nvprof --profile-from-start off python3 src/experiments/uss_pipeline.py 2>> $LOG_FILE
else
    echo "nvprof not found. Skipping detailed kernel profiling." | tee -a $LOG_FILE
fi

# 4. Nsight Compute (SM89 Specific)
if command -v ncu &> /dev/null
then
    echo "--- Nsight Compute (SM89 Analysis) ---" | tee -a $LOG_FILE
    ncu --target-processes all --metrics smsp__sass_thread_inst_executed_op_fadd_pred_on.sum python3 src/experiments/uss_pipeline.py >> $LOG_FILE
fi

echo "Profiling Complete. Results saved to $LOG_FILE"
