#!/bin/bash

# Force BST timezone
export TZ="America/Chicago"

# Path to your JAR file
JAR_PATH="/run/media/dakto/minecraft/WXT Server/spigot.jar"

# Java command as an array
JAVA_CMD=(java
    -XX:+UseG1GC
    -XX:+ParallelRefProcEnabled
    -XX:MaxGCPauseMillis=200
    -XX:+UnlockExperimentalVMOptions
    -XX:+DisableExplicitGC
    -XX:+AlwaysPreTouch
    -XX:G1HeapWastePercent=5
    -XX:G1MixedGCCountTarget=4
    -XX:G1MixedGCLiveThresholdPercent=90
    -XX:G1RSetUpdatingPauseTimePercent=5
    -XX:SurvivorRatio=32
    -XX:+PerfDisableSharedMem
    -XX:MaxTenuringThreshold=1
    -XX:G1NewSizePercent=30
    -XX:G1MaxNewSizePercent=40
    -XX:G1HeapRegionSize=8M
    -XX:G1ReservePercent=20
    -XX:InitiatingHeapOccupancyPercent=15
    -Dusing.aikars.flags=https://mcflags.emc.gs
    -Daikars.new.flags=true
    -jar "$JAR_PATH"
)

# Named screen session
SCREEN_NAME="minecraft"

# Prevent duplicate messages
LAST_MSG=""
LAST_RUN=""

while true; do
    HOUR=$(date +%H)
    MINUTE=$(date +%M)
    TIME_NOW="${HOUR}:${MINUTE}"

    # 3:13 PM warning
    if [ "$TIME_NOW" = "15:13" ] && [ "$LAST_MSG" != "$TIME_NOW" ]; then
        echo "[$TIME_NOW BST] Sending 2-minute warning..."
        screen -S "$SCREEN_NAME" -X stuff "say Server restarting in 2 minutes$(printf \\r)"
        LAST_MSG="$TIME_NOW"
    fi

    # 3:15 PM restart
    if [ "$TIME_NOW" = "15:15" ] && [ "$LAST_RUN" != "$TIME_NOW" ]; then
        echo "[$TIME_NOW BST] Announcing restart and restarting server..."

        # Send restart message to server
        screen -S "$SCREEN_NAME" -X stuff "say Restarting now$(printf \\r)"
        sleep 1

        # Send stop command to server
        screen -S "$SCREEN_NAME" -X stuff "stop$(printf \\r)"
        echo "Sent 'stop' command to Minecraft server."

        # Wait for the screen session to terminate (max 30 seconds)
        for i in {1..30}; do
            if ! screen -list | grep -q "$SCREEN_NAME"; then
                echo "Server stopped."
                break
            fi
            echo "Waiting for server to stop... ($i/30)"
            sleep 1
        done

        # Start Minecraft server in a new screen session
        echo "Starting Minecraft server in screen session '$SCREEN_NAME'..."
        screen -dmS "$SCREEN_NAME" bash -c "$(printf "%q " "${JAVA_CMD[@]}")"

        LAST_RUN="$TIME_NOW"
    fi

    echo "[$(date +%H:%M)] Waiting... (Last restart: $LAST_RUN, Last message: $LAST_MSG)"
    sleep 30
done
