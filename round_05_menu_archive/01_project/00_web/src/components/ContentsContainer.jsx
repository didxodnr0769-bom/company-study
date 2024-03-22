import { useEffect, useState } from "react";
import ContentItem from "./ContentItem";
import { getMenuList } from "../system/api";

/**
 * [Layout] - ContentsContainer
 */
const ContentsContainer = () => {
  const [contents, setContents] = useState([]);
  useEffect(() => {
    getMenuList().then((res) => {
      setContents(res.result.menu_list || []);
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
