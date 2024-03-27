import { useEffect, useState } from "react";
import ContentItem from "./ContentItem";
import { getMenuList } from "../system/api";

/**
 * [Layout] - ContentsContainer
 */
const ContentsContainer = () => {
  const [contents, setContents] = useState([]);
  useEffect(() => {
    // 현재 리스트 API 미구현
    getMenuList().then((res) => {
      setContents(res.data || []);
    });
  }, []);

  return (
    <div className="contents-container">
      {contents.map((content, index) => {
        return <ContentItem key={index} content={content} />;
      })}
    </div>
  );
};

export default ContentsContainer;
