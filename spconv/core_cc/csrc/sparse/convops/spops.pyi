from typing import overload, Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union
from pccm.stubs import EnumValue, EnumClassValue
from cumm.tensorview import Tensor
from cumm.tensorview import CUDAKernelTimer
class ConvGemmOps:
    @staticmethod
    def get_compute_capability(index: int = -1) -> Tuple[int, int]: 
        """
        Args:
            index: 
        """
        ...
    @staticmethod
    def indice_conv(allocator, ext_mm, gemm_tuner, all_w_is_krsc: bool, filter_hwio: bool, features: Tensor, filters: Tensor, indice_pairs: Tensor, indice_pair_num: Tensor, num_activate_out: int, inverse: bool = False, subm: bool = False, algo: int = 0, stream_int: int = 0) -> None: 
        """
        1. this function need to take a out features
        that from subm first mm.
        2. this function don't support CPU.
        Args:
            allocator: 
            ext_mm: 
            gemm_tuner: 
            all_w_is_krsc: 
            filter_hwio: 
            features: 
            filters: 
            indice_pairs: 
            indice_pair_num: 
            num_activate_out: 
            inverse: 
            subm: 
            algo: 
            stream_int: 
        """
        ...
    @staticmethod
    def indice_conv_backward(allocator, ext_mm, gemm_tuner, all_w_is_krsc: bool, filter_hwio: bool, features: Tensor, filters: Tensor, out_bp: Tensor, indice_pairs: Tensor, indice_pair_num: Tensor, inverse: bool = False, subm: bool = False, algo: int = 0, stream_int: int = 0) -> None: 
        """
        Args:
            allocator: 
            ext_mm: 
            gemm_tuner: 
            all_w_is_krsc: 
            filter_hwio: 
            features: 
            filters: 
            out_bp: 
            indice_pairs: 
            indice_pair_num: 
            inverse: 
            subm: 
            algo: 
            stream_int: 
        """
        ...
    @staticmethod
    def implicit_gemm(allocator, conv_tuner, features: Tensor, filters: Tensor, pair_fwd: Tensor, pair_mask_fwd_splits: List[Tensor], mask_argsort_fwd_splits: List[Tensor], num_activate_out: int, masks: Tensor, is_train: bool = False, is_subm: bool = False, stream_int: int = 0, timer: CUDAKernelTimer =  CUDAKernelTimer(False), auto_fp32_accum: bool = True, fp32_accum: bool = False) -> int: 
        """
        Args:
            allocator: 
            conv_tuner: 
            features: 
            filters: 
            pair_fwd: 
            pair_mask_fwd_splits: 
            mask_argsort_fwd_splits: 
            num_activate_out: 
            masks: 
            is_train: 
            is_subm: 
            stream_int: 
            timer: 
            auto_fp32_accum: 
            fp32_accum: 
        """
        ...
    @staticmethod
    def implicit_gemm_backward(allocator, conv_tuner, features: Tensor, filters: Tensor, out_bp: Tensor, pair_fwd: Tensor, pair_bwd: Tensor, pair_mask_fwd_splits: List[Tensor], pair_mask_bwd_splits: List[Tensor], mask_argsort_fwd_splits: List[Tensor], mask_argsort_bwd_splits: List[Tensor], mask_output_fwd: Tensor, masks: Tensor, mask_width: int, is_subm: bool, stream_int: int = 0, timer: CUDAKernelTimer =  CUDAKernelTimer(False), auto_fp32_accum: bool = True, fp32_accum: bool = False) -> None: 
        """
        Args:
            allocator: 
            conv_tuner: 
            features: 
            filters: 
            out_bp: 
            pair_fwd: 
            pair_bwd: 
            pair_mask_fwd_splits: 
            pair_mask_bwd_splits: 
            mask_argsort_fwd_splits: 
            mask_argsort_bwd_splits: 
            mask_output_fwd: 
            masks: 
            mask_width: 
            is_subm: 
            stream_int: 
            timer: 
            auto_fp32_accum: 
            fp32_accum: 
        """
        ...
