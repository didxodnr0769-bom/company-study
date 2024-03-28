import { useEffect, useState } from "react";
import ContentItem from "./ContentItem";
import { getMenuList } from "../system/api";

/**
 * [Layout] - ContentsContainer
 */
const ContentsContainer = () => {
  const [contents, setContents] = useState([]);
  useEffect(() => {
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "visible") {
        getData();
        // 필요한 작업 수행
      } else {
        console.log("웹 애플리케이션이 백그라운드로 전환되었습니다.");
      }
    });

    getData();
  }, []);

  /**
   * 메뉴 목록 조회
   */
  const getData = () => {
    getMenuList().then((res) => {
      setContents(res.data || []);
    });
  };

  return (
    <div className="contents-container">
      {contents.map((content, index) => {
        return <ContentItem key={index} content={content} />;
      })}
    </div>
  );
};

export default ContentsContainer;
