from numba.cuda.cudadrv import nvrtc
from numba.cuda.testing import skip_on_cudasim

import unittest


@skip_on_cudasim("NVVM Driver unsupported in the simulator")
class TestArchOption(unittest.TestCase):
    def test_get_arch_option(self):
        # Test returning the nearest lowest arch.
        self.assertEqual(nvrtc.get_arch_option(7, 5), "compute_75")
        self.assertEqual(nvrtc.get_arch_option(7, 7), "compute_75")
        self.assertEqual(nvrtc.get_arch_option(8, 5), "compute_80")
        self.assertEqual(nvrtc.get_arch_option(9, 1), "compute_90")
        # Test known arch.
        supported_cc = nvrtc.NVRTC().get_supported_archs()
        for arch in supported_cc:
            self.assertEqual(
                nvrtc.get_arch_option(*arch), "compute_%d%d" % arch
            )
        self.assertEqual(
            nvrtc.get_arch_option(1000, 0), "compute_%d%d" % supported_cc[-1]
        )


if __name__ == "__main__":
    unittest.main()
