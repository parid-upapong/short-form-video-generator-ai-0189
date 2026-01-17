#!/bin/bash
# Simple script to trigger 10 concurrent renders to test system stress

API_URL="http://api.viralflow.ai/v1/clips/generate"
VIDEO_URL="https://viral-flow-public.s3.amazonaws.com/test-assets/heavy_4k_test.mp4"

echo "Starting Stress Test: 10 Concurrent Requests..."

for i in {1..10}
do
   curl -X POST $API_URL \
   -H "Content-Type: application/json" \
   -d "{\"video_url\": \"$VIDEO_URL\", \"clip_definitions\": [{\"start_time\": 0, \"end_time\": 15}]}" &
done

wait
echo "All requests dispatched. Check Grafana for GPU saturation."