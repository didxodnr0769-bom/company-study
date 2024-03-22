import ContentsContainer from "./components/ContentsContainer";
import Header from "./components/Header";

/**
 * 앱 메인 컨테이너
 */
function App() {
  return (
    <div>
      {/* Layout - Header */}
      <Header />

      {/* Contents - 메뉴 목록 */}
      <ContentsContainer />
    </div>
  );
}

export default App;
