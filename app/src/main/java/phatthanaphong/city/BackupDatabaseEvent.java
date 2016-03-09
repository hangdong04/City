package phatthanaphong.city;

/**
 * Created by Phatthanaphong on 9/3/2559.
 */
public class BackupDatabaseEvent {
    private int mCommand;
    public static final int BACKUP_DATABASE = 1;

    public BackupDatabaseEvent(int command) {
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
