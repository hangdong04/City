package phatthanaphong.city;

/**
 * Created by phatthanaphong on 20/1/2559.
 */
public class NotifyLocationEvent {
	private int mCommand;
	public static final int LOCATION_CHANGE = 1;

	public NotifyLocationEvent(int command) {
		mCommand = command;
	}

	public int getCommand() {
		return mCommand;
	}

	@Override
	public String toString() {
		return "AppBehaviorEvent{" +
				"mCommand=" + mCommand +
				'}';
	}
}
