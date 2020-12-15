import pytest
import numpy as np
from ase.spacegroup import Spacegroup
from ase.lattice import FCC
from ase.spacegroup.spacegroup import parse_sitesym, parse_sitesym_single, parse_sitesym_element


def test_spacegroup_miscellaneous():
    no = 225
    sg = Spacegroup(no)
    assert int(sg) == no == sg.no
    assert sg.centrosymmetric
    assert sg.symbol == 'F m -3 m'
    assert sg.symbol in str(sg)
    assert sg.lattice == 'F'  # face-centered
    assert sg.setting == 1
    assert sg.scaled_primitive_cell == pytest.approx(FCC(1.0).tocell()[:])
    assert sg.reciprocal_cell @ sg.scaled_primitive_cell == pytest.approx(
        np.identity(3))


def test_spacegroup_parse_sitesym():
    sitesyms = ["x,y,z", "0.25-y,x+1/4,-z", "x-1/4, y+3/4,   1/8-z"]
    expected_trans = np.array(
        [
            [+0.000, 0.000, 0.000],  # x, y, z
            [+0.250, 0.250, 0.000],  # 0.25-y, x+1/4, -z
            [-0.250, 0.750, 0.125]   # x-1/4, y+3/4, 1/8-z
        ],
        dtype=float
    )
    expected_trans_bounded = expected_trans.copy()
    expected_trans_bounded[2, 0] = 0.75
    expected_rot = np.array(
        [
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],  # x, y, z
            [[0, -1, 0], [1, 0, 0], [0, 0, -1]],  # 0.25-y, x+1/4, -z
            [[1, 0, 0], [0, 1, 0], [0, 0, -1]]  # x-1/4, y+3/4, 1/8-z
        ],
        dtype=int
    )

    rot, trans = parse_sitesym(sitesyms)
    rot_bounded, trans_bounded = parse_sitesym(sitesyms, force_positive_translation=True)
    assert np.allclose(rot, expected_rot)
    assert np.allclose(rot_bounded, expected_rot)
    assert np.allclose(trans, expected_trans)
    assert np.allclose(trans_bounded, expected_trans_bounded)


def test_spacegroup_parse_sitesym_single():
    sitesym = "0.125-y,x-1/4,-z"
    expected_rot = np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]], dtype=int)
    expected_trans = np.array([0.125, -0.25, 0.0], dtype=float)
    rot = np.zeros((3, 3), dtype=int)
    trans = np.zeros(3, dtype=float)
    parse_sitesym_single(sitesym, out_rot=rot, out_trans=trans)
    assert np.allclose(rot, expected_rot)
    assert np.allclose(trans, expected_trans)


def test_spacegroup_parse_sitesym_element():
    element_list = ("x", "y", "z", "-x", "0.1+x", "-y-1/8", "+1/2-z")
    expected_rot_list = ((0, 1), (1, 1), (2, 1), (0, -1), (0, 1), (1, -1), (2, -1))
    expected_trans_list = (0.0, 0.0, 0.0, 0.0, 0.1, -0.125, 0.5)

    for element, expected_rot, expected_trans in zip(element_list, expected_rot_list, expected_trans_list):
        rot, trans = parse_sitesym_element(element)
        assert np.allclose(rot, expected_rot)
        assert np.allclose(trans, expected_trans)
