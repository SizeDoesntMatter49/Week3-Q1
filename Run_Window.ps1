
echo "Running Test..."
echo "======================================"

.\Tester\eval_quiz.exe

Remove-Item .\tester\mock_files -Recurse -Force
echo ""
echo "Test completed!"
