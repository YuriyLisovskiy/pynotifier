"""py-notifier tests."""
import pytest

from pynotifier import Notification

osx = pytest.mark.skipif("sys.platform != 'darwin'")


@osx
def test_osx(mocker):
    """Tests pync is imported and called on OSX."""
    pync = mocker.patch("pync.notify")
    Notification(
        title="OSX Title",
        description="OSX Description",
    ).send()
    pync.assert_called_with(message="OSX Description", title="OSX Title", appIcon=None)


@osx
def test_linux_fails_on_osx(mocker):
    """Tests linux fails on OSX because notify-send is not on the PATH."""
    system = mocker.patch("platform.system")
    system.return_value = "Linux"

    with pytest.raises(SystemError):
        Notification(
            title="Notification Title",
            description="Notification Description",
        ).send()
